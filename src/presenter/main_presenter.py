from typing import Optional

from PySide6.QtCore import QObject

from src.core.enums import AccountPermissionEnum
from src.model.main_model import MainModel
from src.presenter import (
    chart_presenter,
    database_presenter,
    home_presenter,
    login_presenter,
    retrieval_presenter,
    setting_presenter,
    storage_presenter,
    )
from src.view.main_view import MainView
from src.view.splash_view import SplashView


class MainPresenter(QObject):
    def __init__(self):
        super().__init__()
        self._is_login: bool = False
        self._current_account_permission: Optional[AccountPermissionEnum] = None

        self._splash_view = SplashView()

        self._splash_view.show_message("正在加载出库模块...(1/8)")
        self._retrieval_presenter = retrieval_presenter.RetrievalPresenter()
        self._splash_view.show_message("正在加载入库模块...(2/8)")
        self._storage_presenter = storage_presenter.StoragePresenter()
        self._splash_view.show_message("正在加载主页模块...(3/8)")
        self._home_presenter = home_presenter.HomePresenter()
        self._splash_view.show_message("正在加载设置模块...(4/8)")
        self._setting_presenter = setting_presenter.SettingPresenter()
        self._splash_view.show_message("正在加载数据库模块...(5/8)")
        self._database_presenter = database_presenter.DatabasePresenter()
        self._splash_view.show_message("正在加载图表模块...(6/8)")
        self._chart_presenter = chart_presenter.ChartPresenter()

        self._splash_view.show_message("正在加载主窗口...(7/8)")

        self._login_presenter = login_presenter.LoginPresenter()
        self._login_presenter.login_status_signal.connect(self._login)
        self._login_presenter.get_view().show()
        while not self._is_login:
            QApplication.processEvents()

        self._view = MainView(
            home_view=self._home_presenter.get_view(),
            storage_view=self._storage_presenter.get_view(),
            retrieval_view=self._retrieval_presenter.get_view(),
            database_view=self._database_presenter.get_view(),
            chart_view=self._chart_presenter.get_view(),
            setting_view=self._setting_presenter.get_view(),
        )

        self._splash_view.show_message("正在初始化主模型...(8/8)")
        self._model = MainModel()
        self._splash_view.show_message("加载完毕,准备启动页面...")

    def get_view(self) -> MainView:
        return self._view

    def get_model(self) -> MainModel:
        return self._model

    def _login(self, is_success: bool) -> bool:
        self._is_login = is_success
        return is_success

    def _show_main_window(self, permission: AccountPermissionEnum) -> None:
        self._view.show()
        self._current_account_permission = permission
        self._view.set_permission(permission)

        if permission == AccountPermissionEnum.Admin:
            self._view.show_admin_tab()
        else:
            self._view.hide_admin_tab()

        self._splash_view.finish(self._view)
        self._splash_view.deleteLater()


if __name__ == "__main__":
    from PySide6.QtWidgets import QApplication

    app = QApplication([])
    presenter = MainPresenter()
    presenter.get_view().show()
    app.exec()
