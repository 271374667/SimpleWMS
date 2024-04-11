import math
from dataclasses import dataclass
from datetime import date, datetime
from typing import List, Optional

from PySide6.QtCore import QAbstractTableModel, QModelIndex, Qt, Signal
from PySide6.QtWidgets import QHeaderView, QVBoxLayout, QWidget
from qfluentwidgets.components import TableView


class MVCTableModel(QAbstractTableModel):
    def __init__(
        self, data: Optional[List] = None, headers: Optional[List[str]] = None
    ):
        super().__init__()
        # 因为要分页,所以一个是所有数据,一个是当前显示的数据
        # 在排序和显示的时候,只对当前显示的数据进行排序和现实
        self._all_data: list[dataclass] = data or []
        self._show_data: list[dataclass] = data or []
        self._headers: list[str] = headers or []

    def rowCount(self, parent=None) -> int:
        return len(self._show_data)

    def columnCount(self, parent=None) -> int:
        return len(self._headers)

    def get_all_data(self) -> list[dataclass]:
        return self._all_data

    def get_data(self) -> list[dataclass]:
        """返回当前显示的本页数据"""
        return self._show_data

    def get_all_data_row_count(self) -> int:
        return len(self._all_data)

    def data(self, index, role=Qt.DisplayRole):
        """
        重写data方法，用于显示数据,这里因为datetime和date和int类型无法直接显示，所以需要转换为str
        """
        if role == Qt.DisplayRole:
            value = getattr(self._show_data[index.row()], self._headers[index.column()])
            if isinstance(value, date):
                return value.strftime("%Y-%m-%d")
            elif isinstance(value, datetime):
                return value.strftime("%Y-%m-%d %H:%M:%S")
            elif isinstance(value, int):
                return str(value)
            else:
                return value

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return self._headers[section]

    def set_header(self, headers: List[str]) -> None:
        self._headers = headers
        self.headerDataChanged.emit(Qt.Horizontal, 0, self.columnCount())

    def set_data_range(
        self, start_num: Optional[int] = None, end_num: Optional[int] = None
    ) -> None:
        """设置显示的数据范围"""
        self.beginResetModel()
        if start_num is None and end_num is None:
            self._show_data = self._all_data
        elif start_num is None:
            self._show_data = self._all_data[:end_num]
        elif end_num is None:
            self._show_data = self._all_data[start_num:]
        else:
            self._show_data = self._all_data[start_num:end_num]
        self.endResetModel()

    def add_row(self, row: dataclass) -> None:
        self.beginInsertRows(QModelIndex(), self.rowCount(), self.rowCount())
        self._show_data.append(row)
        self._all_data.append(row)
        self.endInsertRows()

    def clear(self):
        self.beginResetModel()
        self._show_data.clear()
        self._all_data.clear()
        self.endResetModel()

    def sort(self, column: int, order: Qt.SortOrder = Qt.AscendingOrder) -> None:
        """排序

        经过自定义现在支持int、str、datetime、date类型的排序,str类型按照两个属性进行排序: 长度和字典序排序
        """
        self.layoutAboutToBeChanged.emit()

        def sort_key(item):
            value = getattr(item, self._headers[column])
            if isinstance(value, int):
                return value
            elif isinstance(value, str):
                return len(value), value
            elif isinstance(value, (datetime, date)):
                return value.toordinal()
            else:
                return value

        self._show_data.sort(key=sort_key, reverse=(order == Qt.DescendingOrder))
        self.layoutChanged.emit()

    def recovery_data(self):
        self.beginResetModel()
        self._show_data = self._all_data.copy()
        self.endResetModel()

    def __getitem__(self, index):
        return self._show_data[index]

    def __setitem__(self, index, value) -> None:
        self._show_data[index] = value
        self.dataChanged.emit(
            self.createIndex(index, 0), self.createIndex(index, self.columnCount())
        )


class MVCTableView(TableView):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.horizontalHeader().setSortIndicatorShown(True)
        self.horizontalHeader().sortIndicatorChanged.connect(self.sortByColumn)
        self.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

    def set_header(self, headers: list[str]):
        if model := self.model():
            model.set_header(headers)

    def set_model(self, model):
        self.setModel(model)


class MVCTable(QWidget):
    error_message = Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self._total_page: int = 1
        self._per_page_count: int = 10
        self._current_page: int = 1

        self._view: MVCTableView = MVCTableView(parent=self)
        self._model: MVCTableModel = MVCTableModel()
        self._view.set_model(self._model)

        self._main_layout = QVBoxLayout()
        self._main_layout.addWidget(self._view)
        self.setLayout(self._main_layout)

    def get_view(self) -> MVCTableView:
        return self._view

    def get_model(self) -> MVCTableModel:
        return self._model

    def set_dataclass(self, dataclass: dataclass) -> None:
        """根据dataclass设置header"""
        header = [field.name for field in dataclass.__dataclass_fields__.values()]
        self._set_headers(header)

    def set_data(self, data: list[dataclass]) -> None:
        self.get_view().model().beginResetModel()
        self.get_model()._all_data = data
        self.get_model()._show_data = data
        self.get_view().model().endResetModel()
        self.update_table()

    def get_error_message_signal(self) -> Signal:
        return self.error_message

    def get_current_page_data(self) -> list[dataclass]:
        return self.get_model().get_data()

    def get_all_data(self) -> list[dataclass]:
        return self.get_model().get_all_data()

    def add_row(self, row: dataclass) -> None:
        self.get_view().model().beginResetModel()
        self.get_model().add_row(row)
        self.get_view().model().endResetModel()
        self.update_table()
        self.current_page = self._current_page

    def clear(self) -> None:
        self._model.clear()

    def update_table(self) -> None:
        self._total_page = self.total_page  # 重新计算总页数
        start_num: int = (self._current_page - 1) * self.per_page_count
        end_num: int = min(
            self._current_page * self.per_page_count, self.get_model().rowCount()
        )
        # 设置显示的数据
        self.get_model().set_data_range(start_num, end_num)
        self.get_view().model().beginResetModel()

    @property
    def per_page_count(self) -> int:
        return self._per_page_count

    @per_page_count.setter
    def per_page_count(self, value: int) -> None:
        self._per_page_count = value

    @property
    def current_page(self) -> int:
        return self._current_page if self._current_page > 0 else 1

    @current_page.setter
    def current_page(self, value: int) -> None:
        if value < 1 or value > self.total_page:
            self.error_message.emit(f"页码范围错误, 请设置在1到{self.total_page}之间")
            return
        self._current_page = value

        start_num: int = (self._current_page - 1) * self.per_page_count
        end_num: int = min(
            self._current_page * self.per_page_count,
            self.get_model().get_all_data_row_count(),
        )
        # 设置显示的数据
        self.get_model().set_data_range(start_num, end_num)
        self.get_view().model().beginResetModel()

    @property
    def total_page(self) -> int:
        """总页数

        该方法会根据model的item数量和每页数量计算总页数
        """
        model_item_num: int = self.get_model().get_all_data_row_count()
        # 页码 = 总数 / 每页数量 (向上取整)
        return math.ceil(model_item_num / self.per_page_count)

    def _set_headers(self, headers: List[str]) -> None:
        self._model.set_header(headers)
        self._view.set_header(headers)

    def __getitem__(self, item):
        return self._model[item]

    def __setitem__(self, key, value):
        self._model[key] = value


if __name__ == "__main__":
    from PySide6.QtWidgets import QApplication

    @dataclass
    class TestData:
        name: str
        age: int
        birthday: date

    app = QApplication([])
    controller = MVCTable()
    controller.set_dataclass(TestData)
    controller.add_row(TestData("张三", 18, date(2000, 1, 1)))
    controller.add_row(TestData("李四", 20, date(1998, 1, 1)))
    controller.add_row(TestData("王五", 22, date(1996, 1, 1)))
    controller.add_row(TestData("赵六", 100, date(1994, 1, 1)))
    controller.add_row(TestData("赵7", 3000, date(1994, 1, 1)))
    controller.add_row(TestData("赵8", 2600, date(1994, 1, 1)))
    controller.per_page_count = 2
    controller.current_page = 3
    controller.show()
    app.exec()
