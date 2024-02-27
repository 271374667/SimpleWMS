from typing import List, Tuple

from PySide6.QtCore import QObject
from pyecharts.charts.chart import Chart
from pyecharts.globals import CurrentConfig
from pyecharts.globals import ThemeType

CurrentConfig.ONLINE_HOST = "http://127.0.0.1:8000/"


class ChartBase:
    """未来可能会接入其他的绘图三方库"""
    ...


class PyEChartsBase(ChartBase, QObject):
    """PyECharts的基类"""
    # 默认将使用 WALDEN 主题, 这个主题贴近 Fluent
    echarts_theme = ThemeType.WALDEN

    def set_title(self, title: str):
        """设置图表标题"""
        ...

    def set_subtitle(self, subtitle: str):
        """设置图表副标题"""
        ...

    def set_data(self, data: List[Tuple]):
        """设置图表的数据"""
        ...

    def set_xaxis_label(self, labels: List[str]):
        """设置图表的数据x轴标签"""
        ...

    def get_chart(self) -> Chart:
        """获取图标,之后可以调用图表的render方法进行渲染"""
        ...
