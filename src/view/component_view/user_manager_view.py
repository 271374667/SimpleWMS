from PySide6.QtWidgets import QApplication
from qfluentwidgets.components import ComboBox, LineEdit, PushButton, TableWidget
from qframelesswindow import FramelessWindow

from src.interface.Ui_user_manager_component import Ui_Form
from src.view.message_base_view import MessageBaseView


class UserManagerView(FramelessWindow, MessageBaseView):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        permission: list[str] = ["管理员", "查看者", "编辑者"]
        self.ui.ComboBox.addItems(permission)

    def get_username_lineEdit(self) -> LineEdit:
        return self.ui.LineEdit

    def get_password_lineEdit(self) -> LineEdit:
        return self.ui.LineEdit_2

    def get_permission_comboBox(self) -> ComboBox:
        return self.ui.ComboBox

    def get_add_user_button(self) -> PushButton:
        return self.ui.PushButton

    def get_delete_user_button(self) -> PushButton:
        return self.ui.PushButton_2

    def get_table(self) -> TableWidget:
        return self.ui.TableWidget


if __name__ == "__main__":
    app = QApplication([])
    view = UserManagerView()
    view.show()
    app.exec()
