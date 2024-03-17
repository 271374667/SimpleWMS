from src.model.warn_model import WarnModel
from src.view.warn_view import WarnView


class WarnPresenter:
    def __init__(self):
        self._view = WarnView()
        self._model = WarnModel()

    def get_view(self) -> WarnView:
        return self._view

    def get_model(self) -> WarnModel:
        return self._model
