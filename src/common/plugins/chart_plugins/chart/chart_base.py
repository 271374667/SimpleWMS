"""
默认情况下主题均为QChart.ChartTheme.ChartThemeBlueIcy
动画均为QChart.AnimationOption.AllAnimations
"""
from typing import Sequence

from PySide6.QtCharts import QAbstractSeries, QChart, QChartView
from PySide6.QtCore import QAbstractItemModel, Qt
from PySide6.QtCore import QObject
from PySide6.QtGui import QPainter


class ChartModelBase(QObject):
    """模型映射器基类, 用于将数据集映射到图表上"""

    def get_mapper(self) -> QObject:
        raise NotImplementedError('当前方法未实现')

    def get_series(self) -> QAbstractSeries:
        raise NotImplementedError('当前方法未实现')

    def get_model(self) -> QAbstractItemModel:
        raise NotImplementedError('当前方法未实现')

    def set_data(self, data: Sequence, headers: Sequence) -> None:
        """设置数据"""
        raise NotImplementedError('当前方法未实现')

    def is_empty(self) -> bool:
        """判断数据是否为空"""
        raise NotImplementedError('当前方法未实现')

    def _initialize_series(self, chart_series: QAbstractSeries) -> None:
        """定义每一个图标特殊的内容"""
        raise NotImplementedError('当前方法未实现')

    def _initialize_mapper(self, mapper: QObject) -> None:
        """初始化映射器并设置属性"""
        raise NotImplementedError('当前方法未实现')

    def _initialize_model(self, model: QAbstractItemModel, mapper: QObject) -> None:
        """初始化数据模型并设置属性"""
        raise NotImplementedError('当前方法未实现')


class ChartControllerBase(QObject):
    """图表控制器基类, 用于控制图表的行为
    通过传入数据,在这里可以设置图表的标题,主题,动画等
    """

    def __init__(self):
        super().__init__()
        self._model = None
        self._chart_view = None

    def set_title(self, title: str) -> None:
        self._chart_view.chart().setTitle(title)

    def set_theme(self, theme: QChart.ChartTheme) -> None:
        self._chart_view.chart().setTheme(theme)

    def set_animation(self, animation: QChart.AnimationOption) -> None:
        self._chart_view.chart().setAnimationOptions(animation)

    def _initialize_chart_view(self, chart_view: QChartView) -> None:
        """初始化图表视图"""
        chart_view.setRenderHint(QPainter.Antialiasing)
        chart_view.chart().addSeries(self._model.get_series())

        chart = chart_view.chart()
        chart.setTitle('Chart')
        chart.setTheme(QChart.ChartTheme.ChartThemeBlueIcy)
        chart.setAnimationOptions(QChart.AnimationOption.AllAnimations)

    def _initialize_legend(self, chart_view: QChartView) -> None:
        """初始化图例"""
        chart = chart_view.chart()
        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignmentFlag.AlignTop)

    def _initialize_label(self, series: QAbstractSeries):
        raise NotImplementedError('当前方法未实现')


class ChartBase(QObject):
    """图表基类

    该类用于创建各类图表,同时也是对外暴露的接口
    创建一个图表不应该直接调用ChartModel,而是调用ChartBase的子类
    """

    def get_view(self) -> QChartView:
        raise NotImplementedError('当前方法未实现')

    def get_model(self) -> QAbstractItemModel:
        raise NotImplementedError('当前方法未实现')

    def set_title(self, title: str) -> None:
        raise NotImplementedError('当前方法未实现')

    def set_data(self, data: Sequence, headers: Sequence) -> None:
        raise NotImplementedError('当前方法未实现')
