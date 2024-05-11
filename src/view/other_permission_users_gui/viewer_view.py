"""该视图只能查看,不能新增或者出库库存"""

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from qfluentwidgets import FluentIcon as FIF
from qfluentwidgets import FluentWindow

from src.common.plugins.chart_plugins import server
from src.view import (
    chart_view,
    database_view,
    home_view,
    )


class MainView(FluentWindow):
    def __init__(
        self,
        home_view: home_view.HomeView,
        database_view: database_view.DatabaseView,
        chart_view: chart_view.ChartView,
    ):
        super().__init__()

        # create sub interface
        self.homeInterface = home_view
        self.databaseInterface = database_view
        self.chartInterface = chart_view

        self.initNavigation()
        self.initWindow()

    def initNavigation(self):
        self.addSubInterface(self.homeInterface, FIF.HOME, "主页")

        self.navigationInterface.addSeparator()

        self.addSubInterface(
            self.databaseInterface,
            QIcon(":/icons/images/icons/database_administrator.svg"),
            "数据库操作",
        )

        self.addSubInterface(
            self.chartInterface, QIcon(":/icons/images/icons/chart_bar.svg"), "图表"
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
        home_view.HomeView(),
        database_view.DatabaseView(),
        chart_view.ChartView(),
    )
    w.show()
    app.exec()
