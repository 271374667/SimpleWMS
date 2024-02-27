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

    def get_chart(self) -> Chart:
        """获取图标,之后可以调用图表的render方法进行渲染"""
        ...
