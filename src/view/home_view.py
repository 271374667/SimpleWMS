from PySide6.QtWidgets import QApplication
from qfluentwidgets.components import TitleLabel, ToolButton

from src.interface.Ui_home_page import Ui_Form
from src.view.message_base_view import MessageBaseView


class HomeView(MessageBaseView):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.setWindowTitle('Home Page')
        self.setObjectName('HomePage')

    def get_current_batch_label(self) -> TitleLabel:
        return self.ui.TitleLabel_5

    def get_all_batch_label(self) -> TitleLabel:
        return self.ui.TitleLabel_20

    def get_current_wave_label(self) -> TitleLabel:
        return self.ui.TitleLabel_6

    def get_all_wave_label(self) -> TitleLabel:
        return self.ui.TitleLabel_21

    def get_current_item_quantity_label(self) -> TitleLabel:
        return self.ui.TitleLabel

    def get_all_item_quantity_label(self) -> TitleLabel:
        return self.ui.TitleLabel_7

    def get_current_money_label(self) -> TitleLabel:
        return self.ui.TitleLabel_4

    def get_all_money_label(self) -> TitleLabel:
        return self.ui.TitleLabel_8

    def get_current_storage_label(self) -> TitleLabel:
        return self.ui.TitleLabel_2

    def get_all_storage_label(self) -> TitleLabel:
        return self.ui.TitleLabel_9

    def get_current_retrieval_label(self) -> TitleLabel:
        return self.ui.TitleLabel_3

    def get_all_retrieval_label(self) -> TitleLabel:
        return self.ui.TitleLabel_19

    def get_flush_tool_button(self) -> ToolButton:
        return self.ui.ToolButton


if __name__ == '__main__':
    app = QApplication([])
    window = HomeView()
    window.show()
    app.exec()
