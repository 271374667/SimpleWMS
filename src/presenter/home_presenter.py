from src.model.home_model import HomeModel
from src.view.home_view import HomeView


class HomePresenter:
    def __init__(self):
        self._view = HomeView()
        self._model = HomeModel()
        self._flush_all_label()
        self._connect_signal()

    def get_view(self) -> HomeView:
        return self._view

    def get_model(self) -> HomeModel:
        return self._model

    def _flush_all_label(self) -> None:
        ui = self.get_view()
        ui.get_current_batch_label().setText(self.get_model().get_current_batch_name())
        ui.get_current_wave_label().setText(self.get_model().get_current_wave_name())
        ui.get_current_item_quantity_label().setText(str(self.get_model().get_current_item_quantity()))
        ui.get_current_money_label().setText(str(self.get_model().get_current_money()))
        ui.get_current_storage_label().setText(str(self.get_model().get_current_storage()))
        ui.get_current_retrieval_label().setText(str(self.get_model().get_current_retrieval()))
        ui.get_all_batch_label().setText(str(self.get_model().get_all_batch_number()))
        ui.get_all_wave_label().setText(str(self.get_model().get_all_wave_number()))
        ui.get_all_item_quantity_label().setText(str(self.get_model().get_all_item_quantity()))
        ui.get_all_money_label().setText(str(self.get_model().get_all_money()))
        ui.get_all_storage_label().setText(str(self.get_model().get_all_storage()))
        ui.get_all_retrieval_label().setText(str(self.get_model().get_all_retrieval()))

    def _connect_signal(self):
        self._view.get_flush_tool_button().clicked.connect(self._flush_all_label)


if __name__ == '__main__':
    from PySide6.QtWidgets import QApplication

    app = QApplication([])
    main_presenter = HomePresenter()
    main_presenter.get_view().show()
    app.exec()
