"""
关于商品的品牌统计

-[ ] 所有的商品的品牌占比百分百饼图
-[ ] 库存中的品牌占比百分比饼图x2(本月和全部)
-[ ] 所有卖出的品牌百分比饼图x2(本月和全部）
-[ ] 最近 30 天内各个品牌的售出情况
"""

from src.common.database.controller.chart_plugin_controller import ChartPluginController
from src.common.plugins.chart_plugins.chart.pie_chart import PieChart
from src.common.plugins.plugin_base import Chart, ChartSet


class BrandChart(Chart):
    chart_title: str = "各个品牌占比"
    chart_subtilte: str = '所有的商品的品牌占比百分百饼图'

    def __init__(self):
        self._controller = ChartPluginController()
        self._data = self._controller.get_count_groupby_brand()
        self._pie_chart = PieChart(self._data, self.chart_title, self.chart_subtilte)

    def get_html(self) -> str:
        return self._pie_chart.get_chart().render_embed()

    get_html.__doc__ = Chart.get_html.__doc__


class BrandChartSet(ChartSet):
    """用于存放所有的品牌统计图"""
    plugin_name: str = '品牌相关数据的统计'

    def _initialize(self) -> None:
        self.chart_list.append(BrandChart())

    def get_description(self) -> str:
        return "这里是品牌相关数据的统计, 这里会从多个角度展示品牌的数据"
