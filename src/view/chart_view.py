from PySide6.QtWidgets import QApplication, QWidget
from qfluentwidgets.components import ComboBox, PrimaryPushButton, StrongBodyLabel, ToolTipFilter
from qframelesswindow.webengine import FramelessWebEngineView

from src.interface.Ui_chart_page import Ui_Form
from src.view.message_base_view import MessageBaseView


class ChartView(MessageBaseView):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle("图表")
        self.setObjectName("chart_view")
        self.initialize()

    def get_plugin_select_comboBox(self) -> ComboBox:
        return self.ui.ComboBox

    def get_chart_select_comboBox(self) -> ComboBox:
        return self.ui.ComboBox_2

    def get_description_label(self) -> StrongBodyLabel:
        return self.ui.StrongBodyLabel

    def get_submit_button(self) -> PrimaryPushButton:
        return self.ui.PrimaryPushButton

    def get_web_view(self) -> FramelessWebEngineView:
        return self.ui.widget_2

    def initialize(self) -> None:
        for each in self.findChildren(QWidget):
            each.installEventFilter(ToolTipFilter(each, 200))


if __name__ == "__main__":
    app = QApplication([])
    retrieval_view = ChartView()
    retrieval_view.show()
    app.exec()
