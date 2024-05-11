from PySide6.QtCore import QObject, Signal

from src.core.enums import AccountPermissionEnum
from src.model.login_model import LoginModel
from src.view.component_view.login_view import LoginView


class LoginPresenter(QObject):
    login_status_signal = Signal(bool)
    user_permission_signal = Signal(AccountPermissionEnum)

    def __init__(self):
        super().__init__()
        self._login_view = LoginView()
        self._login_model = LoginModel()

        self._connect_signals()

    def get_view(self) -> LoginView:
        return self._login_view

    def get_model(self) -> LoginModel:
        return self._login_model

    def login(self, username: str, password: str) -> bool:
        if not self._login_model.check_password(username, password):
            self._login_view.show_login_failed()
            self.login_status_signal.emit(False)
            return False

        account = self._login_model.get_user(username)
        # 经过我的观察有的时候关闭不及时,所以先隐藏再关闭{
        self._login_view.hide()
        self._login_view.close()
        self.user_permission_signal.emit(account.permissions)
        self.login_status_signal.emit(True)
        return True

    def _connect_signals(self) -> None:
        self.get_view().get_login_button().clicked.connect(
            lambda: self.login(
                self.get_view().get_username_lineEdit().text(),
                self.get_view().get_password_lineEdit().text(),
            )
        )


if __name__ == "__main__":
    from PySide6.QtWidgets import QApplication

    app = QApplication([])
    login_presenter = LoginPresenter()
    login_presenter.get_view().show()
    app.exec()
