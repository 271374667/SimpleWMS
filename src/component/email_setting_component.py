from PySide6.QtCore import QUrl, Qt
from PySide6.QtWidgets import QApplication, QVBoxLayout, QWidget
from qfluentwidgets import HyperlinkLabel, LineEdit, MessageBoxBase, PasswordLineEdit, PushButton, SubtitleLabel


class EmailSettingComponent(MessageBoxBase):
    """设置邮箱的组件"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.titleLabel = SubtitleLabel('设置您的邮箱', parent)
        self.email_account = LineEdit(parent)
        self.email_account.setPlaceholderText('输入您的邮箱账号')
        self.email_account.setClearButtonEnabled(True)

        self.email_secret_key = PasswordLineEdit(parent)
        self.email_secret_key.setPlaceholderText('输入您的邮箱密钥(注意不是密码,而是秘钥)')

        self.help_label = HyperlinkLabel('如何设置邮箱?', parent)
        self.help_label.setUrl(QUrl(r"https://zhuanlan.zhihu.com/p/648304984"))

        # add widget to view layout
        self.viewLayout.addWidget(self.titleLabel)
        self.viewLayout.addWidget(self.email_account)
        self.viewLayout.addWidget(self.email_secret_key)
        self.viewLayout.addWidget(self.help_label)

        # change the text of button
        self.yesButton.setText('打开')
        self.cancelButton.setText('取消')

        self.widget.setMinimumWidth(350)
        self.yesButton.setEnabled(False)

        self.yesButton.setText('确认设置')
        self.cancelButton.setText('取消')
        self._connect_signal()

    def valid(self) -> None:
        account = self.email_account.text()
        password = self.email_secret_key.text()

        if account and password:
            self.yesButton.setEnabled(True)

    def _connect_signal(self) -> None:
        self.email_account.textChanged.connect(self.valid)
        self.email_secret_key.textChanged.connect(self.valid)


class Demo(QWidget):

    def __init__(self):
        super().__init__()
        self.hBxoLayout = QVBoxLayout(self)
        self.button = PushButton('打开 URL', self)

        self.resize(600, 600)
        self.hBxoLayout.addWidget(self.button, 0, Qt.AlignCenter)
        self.button.clicked.connect(self.showDialog)

    def showDialog(self):
        w = EmailSettingComponent(self)
        if w.exec():
            print(w.email_account.text(), w.email_secret_key.text())


if __name__ == '__main__':
    app = QApplication([])
    w = Demo()
    w.show()
    app.exec()
