from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QHBoxLayout, QSizePolicy, QVBoxLayout
from qfluentwidgets.components import (
    BodyLabel,
    LineEdit,
    PasswordLineEdit,
    PrimaryPushButton,
    TitleLabel,
    )
from qframelesswindow import FramelessWindow

from src.view.message_base_view import MessageBaseView


class LoginView(FramelessWindow, MessageBaseView):
    login_signal = Signal(str, str)

    def __init__(self):
        super().__init__()
        self._init_ui()

    def get_username_lineEdit(self) -> LineEdit:
        return self._username_lineEdit

    def get_password_lineEdit(self) -> PasswordLineEdit:
        return self._password_lineEdit

    def get_login_button(self) -> PrimaryPushButton:
        return self._login_button

    def show_login_failed(self):
        self.show_mask_dialog("登录失败", "用户名或密码错误")
        self.clear()

    def clear(self):
        self._username_lineEdit.clear()
        self._password_lineEdit.clear()

    def _init_ui(self) -> None:
        self.resize(350, 300)

        self._title_label: TitleLabel = TitleLabel()
        self._title_label.setText("登录")
        self._title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._title_label.setSizePolicy(
            QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        )

        self._username_label: BodyLabel = BodyLabel()
        self._username_label.setText("账号")
        self._username_lineEdit = LineEdit()
        self._username_lineEdit.setPlaceholderText("请输入用户名")

        self._password_label: BodyLabel = BodyLabel()
        self._password_label.setText("密码")
        self._password_lineEdit = PasswordLineEdit()
        self._password_lineEdit.setPlaceholderText("请输入密码")

        self._login_button = PrimaryPushButton()
        self._login_button.setText("登录")

        user_name_layout = QHBoxLayout()
        user_name_layout.addWidget(self._username_label)
        user_name_layout.addWidget(self._username_lineEdit)

        password_layout = QHBoxLayout()
        password_layout.addWidget(self._password_label)
        password_layout.addWidget(self._password_lineEdit)

        main_layout = QVBoxLayout()
        main_layout.addWidget(self._title_label)
        main_layout.addLayout(user_name_layout)
        main_layout.addLayout(password_layout)
        main_layout.addWidget(self._login_button)

        self.setLayout(main_layout)

        self._login_button.clicked.connect(self._login)

    def _login(self):
        username = self._username_lineEdit.text()
        password = self._password_lineEdit.text()
        self.login_signal.emit(username, password)


if __name__ == "__main__":
    from PySide6.QtWidgets import QApplication

    app = QApplication([])
    view = LoginView()
    view.show()
    app.exec()
