from src.model import main_model
from src.presenter import retrieval_presenter, storage_presenter
from src.view import (chart_view, database_view, home_view, main_view, setting_view, warn_view)


class MainPresenter:
    def __init__(self):
        self._retrieval_presenter = retrieval_presenter.RetrievalPresenter()
        self._storage_presenter = storage_presenter.StoragePresenter()

        self._view = main_view.MainView(
                home_view=home_view.HomeView(),
                storage_view=self._storage_presenter.get_view(),
                retrieval_view=self._retrieval_presenter.get_view(),
                database_view=database_view.DatabaseView(),
                warn_view=warn_view.WarnView(),
                chart_view=chart_view.ChartView(),
                setting_view=setting_view.SettingView()
                )
        self._model = main_model.MainModel()

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
