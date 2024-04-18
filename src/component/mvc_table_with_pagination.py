"""
这个模块提供了一个带有分页功能的表格组件，主要包括MVCTableWithPagination类。

Classes:
    MVCTableWithPagination: 一个带有分页的表格组件

Usage:
    >>> from src.component.mvc_table_with_pagination import MVCTableWithPagination
    >>> from dataclasses import dataclass
    >>> from datetime import datetime
    >>>
    >>> @dataclass
    >>> class Person:
    >>>     name: str
    >>>     age: int
    >>>     birthday: datetime
    >>>
    >>> table = MVCTableWithPagination()
    >>> table.set_dataclass(Person)
    >>> table.add_row(Person(name="张三", age=18, birthday=datetime.now()))
    >>> table.set_per_page_count(10)
Notes:
    如果你想要运行这个模块，你需要安装下列模块
    "PySide6-Fluent-Widgets[full]>=1.5.3"
    "loguru>=0.7.2"
    "faker>=24.3.0"
"""

from dataclasses import dataclass

from PySide6.QtCore import Signal
from PySide6.QtWidgets import QApplication, QVBoxLayout, QWidget
from qfluentwidgets import TableView

from src.component.mvc_table import MVCTable
from src.component.pagination import Pagination


class MVCTableWithPagination(QWidget):
    """
    一个带有分页的表格

    Attributes:
        _main_layout (QVBoxLayout): 主布局。
        _table (MVCTable): 表格组件。
        _pagination (Pagination): 分页组件。

    Methods:
        set_dataclass(custom_dataclass: dataclass): 设置数据类。
        get_table(): 获取表格。
        get_pagination_error_message_signal(): 获取分页错误信息信号。
        get_table_error_message_signal(): 获取表格错误信息信号。
        add_row(row: dataclass): 添加数据行。
        clear(): 清空表格。
        set_total_pages(total_pages: int): 设置总页数。
        set_per_page_count(per_page_count: int): 设置每页显示的数量。

    Notes:
        1. 通过set_dataclass方法设置数据类
        2. 通过add_row方法添加数据
        3. 通过clear方法清空表格
        4. 通过set_per_page_count方法设置每页显示的数量
        5. 通过get_pagination_error_message_signal方法获取分页错误信息信号
        6. 通过get_table_error_message_signal方法获取表格错误信息信号
    """

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self._main_layout = QVBoxLayout()
        self._table: MVCTable = MVCTable()
        self._pagination: Pagination = Pagination()

        self._main_layout.addWidget(self._table)
        self._main_layout.addWidget(self._pagination)
        self.setLayout(self._main_layout)

        self._pagination.set_total_pages(self._table.total_page)
        self._connect_signal()

    def set_dataclass(self, custom_dataclass: dataclass) -> None:
        self._table.set_dataclass(custom_dataclass)

    def get_table(self) -> TableView:
        return self._table.get_view()

    def get_pagination_error_message_signal(self) -> Signal:
        return self._pagination.get_error_message_signal()

    def get_table_error_message_signal(self) -> Signal:
        return self._table.get_error_message_signal()

    def get_current_page_data(self) -> list[dataclass]:
        return self._table.get_current_page_data()

    def get_all_data(self) -> list[dataclass]:
        return self._table.get_all_data()

    def add_row(self, row: dataclass) -> None:
        self._table.add_row(row)
        self._pagination.set_total_pages(self._table.total_page)

    def clear(self) -> None:
        self._table.clear()

    def set_total_pages(self, total_pages: int) -> None:
        self._pagination.set_total_pages(total_pages)
        self._table.current_page = 1

    def set_per_page_count(self, per_page_count: int) -> None:
        self._table.per_page_count = per_page_count

    def set_data(self, data: list[dataclass]) -> None:
        self._table.set_data(data)
        self._pagination.set_total_pages(self._table.total_page)

    def _set_current_page(self, current_page: int):
        self._table.current_page = current_page

    def _connect_signal(self) -> None:
        # 绑定分页控件和表格
        current_page_signal = self._pagination.get_current_page_signal()
        current_page_signal.connect(self._set_current_page)


if __name__ == "__main__":
    app = QApplication([])
    window = MVCTableWithPagination()
    window.set_total_pages(100)
    window.show()
    app.exec()
