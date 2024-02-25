from typing import Tuple

from PySide6.QtCharts import QAbstractSeries, QBarSeries, QChart, QChartView, QVBarModelMapper
from PySide6.QtGui import QStandardItemModel, Qt

from src.common.plugins.chart_plugins.chart.chart_base import ChartModelBase, ChartControllerBase, ChartBase


class BarChartModel(ChartModelBase):
    def __init__(self):
        super().__init__()
        self._bar_series = QBarSeries()
        self._initialize_series(self._bar_series)
        self._mapper = QVBarModelMapper()
        self._initialize_mapper(self._mapper)
        self._model = QStandardItemModel()
        self._initialize_model(self._model, self._mapper)

    def get_mapper(self) -> QVBarModelMapper:
        return self._mapper

    def get_series(self) -> QBarSeries:
        return self._mapper.series()

    def get_model(self) -> QStandardItemModel:
        return self._mapper.model()

    def set_data(self, data: list[Tuple], headers: list[str]) -> None:
        self._model.setRowCount(len(data))
        self._mapper.setRowCount(self._model.rowCount())
        self._model.setHorizontalHeaderLabels(headers)
        self._model.setColumnCount(len(headers))

        for i, header in enumerate(headers):
            self._model.setHeaderData(i, Qt.Orientation.Horizontal, header)

        row_len = self._model.rowCount()
        col_len = self._model.columnCount()
        for row in range(row_len):
            for col in range(col_len):
                self._model.setData(self._model.index(row, col), data[row][col])

    def is_empty(self) -> bool:
        return self._model.rowCount() == 0

    def _initialize_series(self, chart_series: QBarSeries) -> None:
        pass

    def _initialize_mapper(self, mapper: QVBarModelMapper) -> None:
        mapper.setSeries(self._bar_series)
        # mapper.setFirstBarSetColumn(0)
        # mapper.setFirstRow(0)

    def _initialize_model(self, model: QStandardItemModel, mapper: QVBarModelMapper) -> None:
        mapper.setModel(self._model)


class BarChartController(ChartControllerBase):
    def __init__(self, model: BarChartModel):
        super().__init__()
        self._model = model
        self._chart_view = QChartView()
        self._initialize_chart_view(self._chart_view)

        # 设置图例
        self._initialize_legend(self._chart_view)

        # 设置标签
        self._initialize_label(self._model.get_series())

        # 连接信号

    def get_view(self) -> QChartView:
        return self._chart_view

    def get_model(self) -> QStandardItemModel:
        return self._model.get_model()

    def set_title(self, title: str) -> None:
        self._chart_view.chart().setTitle(title)

    def set_data(self, data: list[Tuple], headers: list[str]) -> None:
        self._model.set_data(data, headers)

    def _initialize_label(self, series: QAbstractSeries):
        ...

    def _initialize_legend(self, chart_view: QChartView):
        ...


class BarChart(ChartBase):
    def __init__(self, data: list[Tuple], headers: list[str]):
        super().__init__()
        self._model = BarChartModel()
        self._model.set_data(data, headers)
        self._controller = BarChartController(self._model)

    def get_view(self) -> QChartView:
        return self._controller.get_view()

    def get_model(self) -> QStandardItemModel:
        return self._controller.get_model()

    def set_title(self, title: str) -> None:
        self._controller.set_title(title)

    def show(self):
        self.get_view().show()


if __name__ == '__main__':
    from PySide6.QtWidgets import QApplication

    app = QApplication([])
    bar = BarChart([('A', 1), ('B', 2), ('C', 3)], ['Label', 'Value'])
    bar.set_title('Bar Chart')
    bar.show()
    app.exec()
