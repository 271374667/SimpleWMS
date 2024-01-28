from src.interface.Ui_retrieval_page import Ui_Form
from PySide6.QtWidgets import QWidget, QApplication
from qfluentwidgets.components import ToolTipFilter


class RetrievalView(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle("出库")
        self.setObjectName("retrieval_view")
        self.initialize()

    def initialize(self) -> None:
        for each in self.findChildren(QWidget):
            each.installEventFilter(ToolTipFilter(each, 200))


if __name__ == "__main__":
    app = QApplication([])
    retrieval_view = RetrievalView()
    retrieval_view.show()
    app.exec()
