from datetime import datetime
from typing import List, Tuple

from PySide6.QtWidgets import QApplication, QLCDNumber, QTableWidgetItem, QWidget
from qfluentwidgets.components import (CompactSpinBox, LineEdit, PlainTextEdit, PushButton, SwitchButton, TableWidget,
                                       ToolTipFilter, TransparentPushButton)

from src.interface.Ui_retrieval_page import Ui_Form
from src.view.message_base_view import MessageBaseView


class RetrievalView(MessageBaseView):
    def __init__(self):
        super().__init__()
        self.table_headers = ['名称', '品牌', '价格', '波次名称', '入库时间', 'EAN13']
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle("出库")
        self.setObjectName("retrieval_view")
        self.initialize()

    def get_is_repeat_switch_button(self) -> SwitchButton:
        return self.ui.SwitchButton

    def get_wave_spinbox(self) -> CompactSpinBox:
        return self.ui.SpinBox_2

    def get_input_lineedit(self) -> LineEdit:
        return self.ui.LineEdit

    def get_confirm_input_button(self) -> PushButton:
        return self.ui.PushButton_2

    def get_output_textedit(self) -> PlainTextEdit:
        return self.ui.PlainTextEdit

    def get_delete_current_row_button(self) -> TransparentPushButton:
        return self.ui.TransparentPushButton_4

    def get_clear_table_button(self) -> TransparentPushButton:
        return self.ui.TransparentPushButton_5

    def get_output_table_button(self) -> TransparentPushButton:
        return self.ui.TransparentPushButton_6

    def get_display_lcd(self) -> QLCDNumber:
        return self.ui.lcdNumber

    def get_table_widget(self) -> TableWidget:
        return self.ui.TableWidget

    def get_auto_wave_switch_button(self) -> SwitchButton:
        return self.ui.SwitchButton_3

    # TODO: 将来表格操作的逻辑都会被放入到utils/table_handler.py中
    def get_data(self) -> List[Tuple[str, str, float, str, str, str]]:
        """获取表格数据"""
        table = self.get_table_widget()
        row_count = table.rowCount()
        data = []
        for i in range(row_count):
            # 如果某一行的数据不完整，那么就跳过这一行
            if self.is_row_empty(i):
                continue

            row_values = self.get_row_values(i)
            data.append((
                    row_values[0],
                    row_values[1],
                    float(row_values[2]),
                    row_values[3],
                    row_values[4],
                    row_values[5]))
        return data

    def add_table_row(self, name: str,
                      brand: str,
                      price: float,
                      batch_name: str,
                      storage_time: datetime,
                      EAN13: str) -> None:
        """添加表格行

        ['名称', '品牌', '价格', '波次名称', '入库时间', 'EAN13']
        """
        table = self.get_table_widget()
        row_count = table.rowCount()
        # 添加的时候优先添加前面空的行
        for i in range(row_count):
            if self.is_row_empty(i):
                row_count = i
                break

        table.insertRow(row_count)
        table.setItem(row_count, 0, QTableWidgetItem(name))
        table.setItem(row_count, 1, QTableWidgetItem(brand))
        table.setItem(row_count, 2, QTableWidgetItem(str(price)))
        table.setItem(row_count, 3, QTableWidgetItem(batch_name))
        table.setItem(row_count, 4, QTableWidgetItem(storage_time.strftime('%Y-%m-%d %H:%M')))
        table.setItem(row_count, 5, QTableWidgetItem(EAN13))

    def is_row_empty(self, row: int) -> bool:
        """判断某一行是否为空"""
        table = self.get_table_widget()
        for i in range(table.columnCount()):
            if table.item(row, i):
                return False
        return True

    def get_row_values(self, row: int) -> list[str]:
        """获取某一行的值"""
        table = self.get_table_widget()
        values = []
        for i in range(table.columnCount()):
            values.append(table.item(row, i).text())
        return values

    def initialize(self) -> None:
        # 将输入框设置可以直接删除
        self.get_input_lineedit().setClearButtonEnabled(True)

        for each in self.findChildren(QWidget):
            each.installEventFilter(ToolTipFilter(each, 200))


if __name__ == "__main__":
    app = QApplication([])
    retrieval_view = RetrievalView()
    retrieval_view.show()
    app.exec()
