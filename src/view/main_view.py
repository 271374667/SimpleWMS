from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from qfluentwidgets import FluentIcon as FIF
from qfluentwidgets import FluentWindow, InfoBadge, InfoBadgePosition, NavigationItemPosition

from src.view import chart_view, database_view, home_view, retrieval_view, setting_view, storage_view, warn_view


class Window(FluentWindow):

    def __init__(self):
        super().__init__()

        # create sub interface
        self.homeInterface = home_view.HomeView()
        self.storageInterface = storage_view.StorageView()
        self.retrievalInterface = retrieval_view.RetrievalView()
        self.databaseInterface = database_view.DatabaseView()
        self.warnInterface = warn_view.WarnView()
        self.chartInterface = chart_view.ChartView()
        self.settingInterface = setting_view.SettingView()

        self.initNavigation()
        self.initWindow()

    def initNavigation(self):
        self.addSubInterface(self.homeInterface, FIF.HOME, '主页')
        self.addSubInterface(self.storageInterface, QIcon(":/icons/images/icons/database_export.svg"), '入库')
        self.addSubInterface(self.retrievalInterface, QIcon(":/icons/images/icons/sign_out.svg"), '出库')

        self.navigationInterface.addSeparator()

        self.addSubInterface(self.databaseInterface, QIcon(":/icons/images/icons/database_administrator.svg"),
                             '数据库操作')

        self.addSubInterface(self.warnInterface, QIcon(":/icons/images/icons/brake_warning.svg"), '预警')
        self.addSubInterface(self.chartInterface, QIcon(":/icons/images/icons/chart_bar.svg"), '图表')

        # add custom widget to bottom

        self.addSubInterface(self.settingInterface, FIF.SETTING, '设置', NavigationItemPosition.BOTTOM)

        # add badge to navigation item
        item = self.navigationInterface.widget(self.homeInterface.objectName())
        InfoBadge.attension(
                text=9,
                parent=item.parent(),
                target=item,
                position=InfoBadgePosition.NAVIGATION_ITEM
                )

        # NOTE: enable acrylic effect
        # self.navigationInterface.setAcrylicEnabled(True)

    def initWindow(self):
        self.resize(1100, 800)
        self.setWindowIcon(QIcon(':/icons/images/icons/area_chart.svg'))
        self.setWindowTitle('SimpleWMS 一个纯粹的仓库管理系统')

        desktop = QApplication.screens()[0].availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.move(w // 2 - self.width() // 2, h // 2 - self.height() // 2)

        # set the minimum window width that allows the navigation panel to be expanded
        # self.navigationInterface.setMinimumExpandWidth(900)
        # self.navigationInterface.expand(useAni=False)


if __name__ == '__main__':
    app = QApplication([])
    w = Window()
    w.show()
    app.exec()
