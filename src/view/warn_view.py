from PySide6.QtWidgets import QApplication, QWidget
from qfluentwidgets.components import SegmentedWidget, StrongBodyLabel, TableWidget, ToolTipFilter

from src.interface.Ui_warn_page import Ui_Form


class WarnView(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.setWindowTitle("预警")
        self.setObjectName("warn_view")

        self._create_widgets()

    def get_segment_widget(self) -> SegmentedWidget:
        return self.ui.SegmentedWidget

    def get_outofstock_table(self) -> TableWidget:
        return self.ui.TableWidget

    def get_outofstock_lable(self) -> StrongBodyLabel:
        return self.ui.StrongBodyLabel

    def get_unsalable_table(self) -> TableWidget:
        return self.ui.TableWidget_2

    def get_unsalable_lable(self) -> StrongBodyLabel:
        return self.ui.StrongBodyLabel_2

    def _create_widgets(self):
        self.ui.SegmentedWidget.addItem("outofstock",
                                        "缺货预警",
                                        onClick=lambda: self.ui.stackedWidget.setCurrentIndex(0)
                                        )

        self.ui.SegmentedWidget.addItem('unsalable',
                                        '滞销预警',
                                        onClick=lambda: self.ui.stackedWidget.setCurrentIndex(1)
                                        )
        self.ui.SegmentedWidget.setCurrentItem('outofstock')

    def initialize(self) -> None:
        for each in self.findChildren(QWidget):
            each.installEventFilter(ToolTipFilter(each, 200))


if __name__ == "__main__":
    app = QApplication([])
    retrieval_view = WarnView()
    retrieval_view.show()
    app.exec()
