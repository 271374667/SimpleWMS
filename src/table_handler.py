"""
因为在这个项目中，有大量的对表格相关的操作,所以都统一封装到这个模块里面,但是其中不会涉及到具体的某个表格
所有的操作都是通用的,默认情况下如果一行中有空值，那么就会跳过这一行,防止数据库中出现空值
其中包括
1. 表格数据的获取
2. 表格数据的添加
3. 表格数据的删除
4. 表格数据的判断
"""

from pathlib import Path
from typing import Optional
from typing import Union

import pandas as pd
from PySide6.QtCore import QObject, Signal
from PySide6.QtWidgets import QTableWidgetItem
from qfluentwidgets.components import TableWidget

from src.dict_typing import CustomBaseDict


class TableHandler(QObject):
    # 如果出现空行，那么就会发出这个信号,第一个参数是行数，第二个参数是列数
    null_skip_signal = Signal(int, int)

    def __init__(
        self,
        table: TableWidget,
        headers: Optional[CustomBaseDict] = None,
        show_headers: list[str] = None,
    ):
        super().__init__()
        self._table: TableWidget = table

        if headers:
            self._headers: list[str] = list(headers.__annotations__.keys())
        self.show_headers = show_headers

        self.clear()

    def get_table(self) -> TableWidget:
        """获取表格对象"""
        return self._table

    def clear(self) -> None:
        """清空表格,设置行数为20"""
        self._table.clearContents()
        self._table.setRowCount(20)

    def get_data(self) -> list[CustomBaseDict]:
        """获取表格中的所有数据"""
        # TODO: 之后这个方法改成yield
        row_count = self._table.rowCount()
        data = []
        for row_index in range(row_count):
            current_row_data = {}
            if self.is_null(row_index):
                continue
            for column_index in range(len(self._headers)):
                current_row_data[self._headers[column_index]] = self._table.item(
                    row_index, column_index
                ).text()

            data.append(current_row_data)
        return data

    def export_data(self, file_path: Union[Path, str]) -> None:
        """导出表格数据"""
        data = self.get_data()
        df = pd.DataFrame(data)
        # 重新设置列名
        df.columns = self.show_headers
        df.to_excel(file_path, index=False)

    def get_last_row_index(self) -> int:
        """获取最后一行的索引, 如果有空值那么直接返回上一行的索引"""
        for i in range(self._table.rowCount() - 1):
            if self.is_null(i):
                return i
        return self._table.rowCount() - 1

    def add_row(self, row_data: CustomBaseDict) -> None:
        """添加一行数据"""
        if len(row_data) != len(self._headers):
            raise ValueError("数据长度和表头长度不一致")

        if (row_data is None) or (not isinstance(row_data, dict)) or (row_data == {}):
            return None

        last_row_index = self.get_last_row_index()
        max_row_count = self._table.rowCount()

        if last_row_index == max_row_count - 1:
            self._table.setRowCount(max_row_count + 1)

        for key in row_data:
            self._table.setItem(
                last_row_index,
                self._get_header_index(key),
                QTableWidgetItem(str(row_data[key])),
            )

    def add_rows(self, rows_data: list[CustomBaseDict]) -> None:
        """添加多行数据"""
        if not rows_data or not isinstance(rows_data, list):
            return None

        last_row_index = self.get_last_row_index()
        max_row_count = self._table.rowCount()
        data_length = len(rows_data)

        if last_row_index + data_length >= max_row_count:
            self._table.setRowCount(max_row_count + data_length)

        for row_index in range(data_length):
            for key in rows_data[row_index]:
                self._table.setItem(
                    last_row_index + row_index,
                    self._get_header_index(key),
                    QTableWidgetItem(str(rows_data[row_index][key])),
                )

    def set_data(self, data: list[CustomBaseDict]) -> None:
        """设置表格数据"""
        self.clear()
        self.add_rows(data)

    def set_headers(self, headers: CustomBaseDict) -> None:
        """设置表头"""
        if headers:
            self._headers = list(headers.__annotations__.keys())

    def set_show_headers(self, show_headers: list[str]) -> None:
        """设置展示给用户的表头"""
        if self._table.columnCount() != len(show_headers):
            self._table.setColumnCount(len(show_headers))

        self._table.setHorizontalHeaderLabels(show_headers)
        self.show_headers = show_headers

    def scroll_to_row(self, row_index: int) -> None:
        """滚动到指定行"""
        self._table.scrollToItem(self._table.item(row_index, 0))

    def is_null(self, row_index: int, column_index: int = None) -> bool:
        """判断是存在空值

        判断某个项是否存在空值,如果不填写列数，那么就会判断整行是否存在空值
        如果存在空值，那么就会发出信号,并且返回True,否则返回False
        Args:
            row_index: 行数
            column_index: 列数
        """
        column_count = self._table.columnCount()
        if column_index is None:
            for column_index_loop in range(column_count):
                if not self._table.item(row_index, column_index_loop):
                    self.null_skip_signal.emit(row_index, column_index)
                    return True
        elif not self._table.item(row_index, column_index):
            self.null_skip_signal.emit(row_index, column_index)
            return True
        return False

    def _get_header_index(self, header: str) -> Union[int, None]:
        """获取表头的索引"""
        try:
            return self._headers.index(header)
        except ValueError:
            return None
