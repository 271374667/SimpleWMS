from PySide6.QtCore import Signal, QObject

from src.model.login_model import LoginModel
from src.view.component_view.login_view import LoginView


class LoginPresenter(QObject):
    login_status_signal = Signal(bool)

    def __init__(self):
        super().__init__()
        self._login_view = LoginView()
        self._login_model = LoginModel()

        self._connect_signals()

    def get_view(self) -> LoginView:
        return self._login_view

    def login(self, username: str, password: str) -> bool:
        if not self._login_model.check_password(username, password):
            self._login_view.show_login_failed()
            self.login_status_signal.emit(False)
            return False

        self._login_view.close()
        self.login_status_signal.emit(True)
        return True

    def _connect_signals(self) -> None:
        self._login_view.login_signal.connect(self.login)


if __name__ == "__main__":
    from PySide6.QtWidgets import QApplication

    app = QApplication([])
    login_presenter = LoginPresenter()
    login_presenter.get_view().show()
    app.exec()
