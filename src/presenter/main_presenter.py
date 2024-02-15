from src.model import main_model
from src.presenter import database_presenter, home_presenter, retrieval_presenter, setting_presenter, storage_presenter
from src.view import (chart_view, main_view)
from src.component.splashwindow import SplashWindow


class MainPresenter:
    def __init__(self):
        self._retrieval_presenter = retrieval_presenter.RetrievalPresenter()
        self._storage_presenter = storage_presenter.StoragePresenter()
        self._home_presenter = home_presenter.HomePresenter()
        self._setting_presenter = setting_presenter.SettingPresenter()
        self._database_presenter = database_presenter.DatabasePresenter()

        self._view = main_view.MainView(
                home_view=self._home_presenter.get_view(),
                storage_view=self._storage_presenter.get_view(),
                retrieval_view=self._retrieval_presenter.get_view(),
                database_view=self._database_presenter.get_view(),
                chart_view=chart_view.ChartView(),
                setting_view=self._setting_presenter.get_view()
                )
        self._model = main_model.MainModel()

        # 关闭启动图片
        SplashWindow.close_splash()

    def get_view(self) -> main_view.MainView:
        return self._view

    def get_model(self) -> main_model.MainModel:
        return self._model


if __name__ == '__main__':
    from PySide6.QtWidgets import QApplication

    app = QApplication([])
    presenter = MainPresenter()
    presenter.get_view().show()
    app.exec()
