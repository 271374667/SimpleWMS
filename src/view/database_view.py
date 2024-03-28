from PySide6.QtCore import Qt
from PySide6.QtGui import QAction, QCursor
from PySide6.QtWidgets import QApplication, QWidget
from qfluentwidgets import FluentIcon, Icon, MenuAnimationType, RoundMenu
from qfluentwidgets.components import (
    ComboBox,
    PrimaryPushButton,
    StrongBodyLabel,
    TableWidget,
    ToolTipFilter,
)

from src.interface.Ui_database_page import Ui_Form
from src.view.message_base_view import MessageBaseView
from src.component.pagination import Pagination


class DatabaseView(MessageBaseView):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle("数据库")
        self.setObjectName("database_view")
        self.initialize()

        self._create_menu()

    def get_plugin_select_comboBox(self) -> ComboBox:
        return self.ui.ComboBox

    def get_table(self) -> TableWidget:
        return self.ui.TableWidget

    def get_pagination(self) -> Pagination:
        return self.ui.widget_2

    def get_custom_widget(self) -> QWidget:
        return self.ui.widget

    def get_description_label(self) -> StrongBodyLabel:
        return self.ui.StrongBodyLabel

    def get_submit_button(self) -> PrimaryPushButton:
        return self.ui.PrimaryPushButton

    def get_refresh_action(self) -> QAction:
        return self._refresh_action

    def get_export_action(self) -> QAction:
        return self._export_action

    def initialize(self) -> None:
        self.get_table().customContextMenuRequested.connect(self._show_menu)

        for each in self.findChildren(QWidget):
            each.installEventFilter(ToolTipFilter(each, 200))

    def _create_menu(self) -> None:
        """创建右键菜单"""
        tb = self.get_table()
        tb.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)

        self._round_menu = RoundMenu(parent=tb)
        self._refresh_action = QAction("刷新")
        self._refresh_action.setIcon(Icon(FluentIcon.SYNC))
        self._round_menu.addAction(self._refresh_action)

        self._export_action = QAction("导出")
        self._export_action.setIcon(Icon(FluentIcon.EMBED))
        self._round_menu.addAction(self._export_action)

    def _show_menu(self, pos):
        self._round_menu.exec(QCursor.pos(), aniType=MenuAnimationType.DROP_DOWN)


if __name__ == "__main__":
    app = QApplication([])
    retrieval_view = DatabaseView()
    retrieval_view.show()
    app.exec()
