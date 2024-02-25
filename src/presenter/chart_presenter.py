from src.model.chart_model import ChartModel
from src.view.chart_view import ChartView


class ChartPresenter:
    def __init__(self):
        self._view = ChartView()
        self._model = ChartModel()

    def get_view(self) -> ChartView:
        return self._view

    def get_model(self) -> ChartModel:
        return self._model
