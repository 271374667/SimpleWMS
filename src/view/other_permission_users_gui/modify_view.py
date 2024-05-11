"""该视图只能出库和入库,无法查看库存信息"""

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from qfluentwidgets import FluentWindow

from src.common.plugins.chart_plugins import server
from src.view import (
    retrieval_view,
    storage_view,
    )


class MainView(FluentWindow):
    def __init__(
        self,
        storage_view: storage_view.StorageView,
        retrieval_view: retrieval_view.RetrievalView,
    ):
        super().__init__()

        # create sub interface
        self.storageInterface = storage_view
        self.retrievalInterface = retrieval_view

        self.initNavigation()
        self.initWindow()

    def initNavigation(self):
        self.addSubInterface(
            self.storageInterface,
            QIcon(":/icons/images/icons/database_export.svg"),
            "入库",
        )
        self.addSubInterface(
            self.retrievalInterface, QIcon(":/icons/images/icons/sign_out.svg"), "出库"
        )

    def initWindow(self):
        self.resize(1100, 800)
        self.setWindowIcon(QIcon(":/icons/images/icons/area_chart.svg"))
        self.setWindowTitle("SimpleWMS 一个纯粹的仓库管理系统")

        desktop = QApplication.screens()[0].availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.move(w // 2 - self.width() // 2, h // 2 - self.height() // 2)
        self.setStyleSheet("background-color: #fcfcfc")

    def closeEvent(self, event):
        server.stop()
        event.accept()


if __name__ == "__main__":
    app = QApplication([])
    w = MainView(
        storage_view.StorageView(),
        retrieval_view.RetrievalView(),
    )
    w.show()
    app.exec()
