from dataclasses import dataclass
from datetime import date, datetime
from typing import List, Optional

from PySide6.QtCore import QAbstractTableModel, QModelIndex, Qt
from PySide6.QtWidgets import QHeaderView, QVBoxLayout, QWidget
from qfluentwidgets.components import TableView


class MVCTableModel(QAbstractTableModel):
    def __init__(
        self, data: Optional[List] = None, headers: Optional[List[str]] = None
    ):
        super().__init__()
        self._data: list[dataclass] = data or []
        self._headers: list[str] = headers or []

    def rowCount(self, parent=None) -> int:
        return len(self._data)

    def columnCount(self, parent=None) -> int:
        return len(self._headers)

    def data(self, index, role=Qt.DisplayRole):
        """
        重写data方法，用于显示数据,这里因为datetime和date和int类型无法直接显示，所以需要转换为str
        """
        if role == Qt.DisplayRole:
            value = getattr(self._data[index.row()], self._headers[index.column()])
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

    def add_row(self, row: dataclass) -> None:
        self.beginInsertRows(QModelIndex(), self.rowCount(), self.rowCount())
        self._data.append(row)
        self.endInsertRows()

    def clear(self):
        self.beginResetModel()
        self._data.clear()
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
            elif isinstance(value, datetime) or isinstance(value, date):
                return value.toordinal()
            else:
                return value

        self._data.sort(key=sort_key, reverse=(order == Qt.DescendingOrder))
        self.layoutChanged.emit()

    def __getitem__(self, index):
        return self._data[index]

    def __setitem__(self, index, value) -> None:
        self._data[index] = value
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
        model = self.model()
        if model:
            model.set_header(headers)

    def set_model(self, model):
        self.setModel(model)


class MVCTableController(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
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

    def add_row(self, row: dataclass) -> None:
        self.get_view().model().add_row(row)

    def clear(self) -> None:
        self._model.clear()

    def _set_headers(self, headers: List[str]) -> None:
        self._model.set_header(headers)
        self._view.set_header(headers)


if __name__ == "__main__":
    from PySide6.QtWidgets import QApplication

    @dataclass
    class TestData:
        name: str
        age: int
        birthday: date

    app = QApplication([])
    controller = MVCTableController()
    controller.set_dataclass(TestData)
    controller.add_row(TestData("张三", 18, date(2000, 1, 1)))
    controller.add_row(TestData("李四", 20, date(1998, 1, 1)))
    controller.add_row(TestData("王五", 22, date(1996, 1, 1)))
    controller.show()
    app.exec()
