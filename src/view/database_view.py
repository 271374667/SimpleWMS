from PySide6.QtWidgets import QApplication, QWidget
from qfluentwidgets.components import ComboBox, PrimaryPushButton, StrongBodyLabel, TableWidget, ToolTipFilter

from src.interface.Ui_database_page import Ui_Form
from src.view.message_base_view import MessageBaseView


class DatabaseView(MessageBaseView):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle("数据库")
        self.setObjectName("database_view")
        self.initialize()

    def get_plugin_select_comboBox(self) -> ComboBox:
        return self.ui.ComboBox

    def get_table(self) -> TableWidget:
        return self.ui.TableWidget

    def get_custom_widget(self) -> QWidget:
        return self.ui.widget

    def get_description_label(self) -> StrongBodyLabel:
        return self.ui.StrongBodyLabel

    def get_submit_button(self) -> PrimaryPushButton:
        return self.ui.PrimaryPushButton

    def initialize(self) -> None:
        for each in self.findChildren(QWidget):
            each.installEventFilter(ToolTipFilter(each, 200))


if __name__ == "__main__":
    app = QApplication([])
    retrieval_view = DatabaseView()
    retrieval_view.show()
    app.exec()
