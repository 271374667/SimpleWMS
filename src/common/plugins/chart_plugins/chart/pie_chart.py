from typing import Tuple

from PySide6.QtCharts import QChartView, QPieSeries, QPieSlice, QVPieModelMapper
from PySide6.QtCore import Qt
from PySide6.QtGui import QStandardItemModel

from src.common.plugins.chart_plugins.chart.chart_base import ChartBase, ChartControllerBase, ChartModelBase


class PieModel(ChartModelBase):
    def __init__(self):
        super().__init__()
        # 定义每一个图标特殊的内容
        self._pie_series = QPieSeries()
        self._initialize_series(self._pie_series)
        # 创建映射器并设置属性
        self._mapper = QVPieModelMapper()
        self._initialize_mapper(self._mapper)
        # 创建数据模型
        self._model = QStandardItemModel()
        self._initialize_model(self._model, self._mapper)

    def get_mapper(self) -> QVPieModelMapper:
        return self._mapper

    def get_series(self) -> QPieSeries:
        return self._mapper.series()

    def get_model(self) -> QStandardItemModel:
        return self._mapper.model()

    def set_data(self, data: list[Tuple[str, int]], headers: Tuple[str, str]) -> None:
        """设置数据"""
        self._model.setRowCount(len(data))
        self._mapper.setRowCount(self._model.rowCount())
        self._model.setHorizontalHeaderLabels(headers)
        self._model.setHeaderData(0, Qt.Orientation.Horizontal, headers[0])
        self._model.setHeaderData(1, Qt.Orientation.Horizontal, headers[1])

        # 添加数据
        for i, (label, value) in enumerate(data):
            self._model.setData(self._model.index(i, 0), label)
            self._model.setData(self._model.index(i, 1), value)

    def is_empty(self) -> bool:
        return self._model.rowCount() == 0

    def _initialize_series(self, chart_series: QPieSeries) -> None:
        """定义每一个图标特殊的内容"""
        chart_series.setHoleSize(0.35)

    def _initialize_mapper(self, mapper: QVPieModelMapper) -> None:
        """初始化映射器并设置属性"""
        # 饼图只需要两列数据, 一列是标签, 一列是值
        mapper.setSeries(self._pie_series)
        mapper.setLabelsColumn(0)
        mapper.setValuesColumn(1)
        mapper.setFirstRow(0)

    def _initialize_model(self, model: QStandardItemModel, mapper: QVPieModelMapper) -> None:
        """初始化数据模型"""
        model.setColumnCount(2)
        mapper.setModel(self._model)


class PieController(ChartControllerBase):
    def __init__(self, model: PieModel):
        super().__init__()
        self._old_label: str = ''  # 因为饼图的悬停效果需要显示当前的值, 所以需要一个变量来保存曾经的文本

        self._model = model
        self._chart_view = QChartView()
        self._initialize_chart_view(self._chart_view)

        # 设置图例
        self._initialize_legend(self._chart_view)

        # 设置标签
        self._initialize_label(self._model.get_series())

        # 连接信号
        self._model.get_series().hovered.connect(self._on_slice_hovered)
        self._model.get_series().clicked.connect(self._on_click_slice)

    def get_view(self) -> QChartView:
        return self._chart_view

    def get_model(self) -> QStandardItemModel:
        return self._model.get_model()

    def _on_slice_hovered(self, pie_slice: QPieSlice, is_hovered: bool) -> None:
        """
        设置饼图的悬停效果, 当鼠标悬停在饼图上时, 饼图会突出显示, 并且鼠标会变成手型
        """
        pie_slice.setExploded(is_hovered)
        chart = self._chart_view.chart()
        if is_hovered:
            self._old_label = pie_slice.label()
            chart.setCursor(Qt.CursorShape.PointingHandCursor)
            pie_slice.setLabelPosition(QPieSlice.LabelPosition.LabelInsideHorizontal)
            pie_slice.setLabel(f'数量:{pie_slice.value()}')
        else:
            chart.setCursor(Qt.CursorShape.ArrowCursor)
            pie_slice.setLabelPosition(QPieSlice.LabelPosition.LabelOutside)
            pie_slice.setLabel(self._old_label)

    def _on_click_slice(self, pie_slice: QPieSlice) -> None:
        """点击会删除slice"""
        self._model.get_series().remove(pie_slice)

    def _initialize_label(self, series: QPieSeries):
        series.setLabelsVisible(True)
        series.setLabelsPosition(QPieSlice.LabelPosition.LabelOutside)
        for each in series.slices():
            each.setLabel(f'{each.label()}:{each.percentage():.2%}')


class PieChart(ChartBase):
    def __init__(self, data: list[Tuple[str, int]], headers: Tuple[str, str]):
        super().__init__()
        self._model = PieModel()
        self._model.set_data(data, headers)
        self._controller = PieController(self._model)

    def get_view(self) -> QChartView:
        return self._controller.get_view()

    def get_model(self) -> QStandardItemModel:
        return self._controller.get_model()

    def set_title(self, title: str) -> None:
        self._controller.set_title(title)

    def show(self) -> None:
        self.get_view().show()


if __name__ == '__main__':
    from PySide6.QtWidgets import QApplication
    from PySide6.QtCharts import QChartView

    app = QApplication([])

    data = [
            ('Apple', 1),
            ('Banana', 2),
            ('Cherry', 3),
            ('Date', 4)
            ]
    headers = ('Label', 'Value')
    pie_chart = PieChart(data, headers)
    pie_chart.set_title('Simple piechart example')
    pie_chart.show()

    print('ok')
    app.exec()
