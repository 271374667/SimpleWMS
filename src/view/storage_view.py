from PySide6.QtWidgets import QApplication, QLCDNumber, QWidget
from qfluentwidgets.components import (CompactDoubleSpinBox, CompactSpinBox, LineEdit, PrimaryPushButton, SwitchButton,
                                       TableWidget, ToolTipFilter, TransparentPushButton)

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

    def get_price_doublespinbox(self) -> CompactDoubleSpinBox:
        return self.ui.CompactDoubleSpinBox

    def get_batch_spinbox(self) -> CompactSpinBox:
        return self.ui.CompactSpinBox

    def get_print_number_spinbox(self) -> CompactSpinBox:
        return self.ui.CompactSpinBox_2

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

    def initialize(self) -> None:
        # 设置输入框可以直接删除
        self.get_clothes_name_lineedit().setClearButtonEnabled(True)
        self.get_brand_lineedit().setClearButtonEnabled(True)

        for each in self.findChildren(QWidget):
            each.installEventFilter(ToolTipFilter(each, 200))


if __name__ == "__main__":
    app = QApplication([])
    retrieval_view = StorageView()
    retrieval_view.show()
    app.exec()
