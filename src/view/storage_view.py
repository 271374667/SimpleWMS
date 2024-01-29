from PySide6.QtWidgets import QApplication, QTableWidgetItem, QWidget, QLCDNumber
from qfluentwidgets.components import (DoubleSpinBox, LineEdit, PrimaryPushButton, SpinBox, SwitchButton, TableWidget,
                                       ToolTipFilter, TransparentPushButton)

from src.interface.Ui_storage_page import Ui_Form
from src.view.message_base_view import MessageBaseView


class StorageView(MessageBaseView):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.setWindowTitle("存储")
        self.setObjectName("storage_view")
        self.initialize()

    def get_clothes_name_lineedit(self) -> LineEdit:
        return self.ui.LineEdit

    def get_brand_lineedit(self) -> LineEdit:
        return self.ui.LineEdit_2

    def get_price_doublespinbox(self) -> DoubleSpinBox:
        return self.ui.DoubleSpinBox

    def get_batch_spinbox(self) -> SpinBox:
        return self.ui.SpinBox_2

    def get_print_number_spinbox(self) -> SpinBox:
        return self.ui.SpinBox

    def get_auto_switch_button(self) -> SwitchButton:
        return self.ui.SwitchButton

    def get_confirm_button(self) -> PrimaryPushButton:
        return self.ui.PrimaryPushButton

    def get_clear_table_button(self) -> TransparentPushButton:
        return self.ui.TransparentPushButton

    def get_save_table_button(self) -> TransparentPushButton:
        return self.ui.TransparentPushButton_3

    def get_delete_current_row_button(self) -> TransparentPushButton:
        return self.ui.TransparentPushButton_4

    def get_table_widget(self) -> TableWidget:
        return self.ui.TableWidget_2

    def get_display_lcd(self) -> QLCDNumber:
        return self.ui.lcdNumber

    def set_table_data(self, data: list[list[str, str, float, int]]) -> None:
        """设置表格数据

        设置表格数据，表格每一次都会被清空，然后重新设置数据,这样确保左侧的序号正确

        Args:
            data: list[list[商品名称, 品牌, 价格, 批次]]
        """
        table = self.get_table_widget()
        table.clear()
        table.setHorizontalHeaderLabels(['商品名称', '品牌', '价格', '批次'])
        table.setRowCount(len(data))
        for i, each in enumerate(data):
            for j, item in enumerate(each):
                table.setItem(i, j, QTableWidgetItem(item))

    def add_table_row(self, name: str, brand: str, price: str, batch: str, quantity: str) -> None:
        """添加表格行

        Args:
            name: 商品名称
            brand: 品牌
            price: 价格
            batch: 批次
            quantity: 数量
        """
        table = self.get_table_widget()
        for _ in range(int(quantity)):
            row_count = table.rowCount()
            # 添加的时候优先添加前面空的行
            for i in range(row_count):
                if (not table.item(i, 0)
                        and not table.item(i, 1)
                        and not table.item(i, 2)
                        and not table.item(i, 3)):
                    row_count = i
                    break

            table.insertRow(row_count)
            table.setItem(row_count, 0, QTableWidgetItem(name))
            table.setItem(row_count, 1, QTableWidgetItem(brand))
            table.setItem(row_count, 2, QTableWidgetItem(price))
            table.setItem(row_count, 3, QTableWidgetItem(batch))
        # 跳转到最后一行

    def initialize(self) -> None:
        for each in self.findChildren(QWidget):
            each.installEventFilter(ToolTipFilter(each, 200))


if __name__ == "__main__":
    app = QApplication([])
    retrieval_view = StorageView()
    retrieval_view.show()
    app.exec()
