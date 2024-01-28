from PySide6.QtWidgets import QApplication, QWidget

from src.interface.Ui_home_page import Ui_Form


class HomeView(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.setWindowTitle('Home Page')
        self.setObjectName('HomePage')


if __name__ == '__main__':
    app = QApplication([])
    window = HomeView()
    window.show()
    app.exec()
