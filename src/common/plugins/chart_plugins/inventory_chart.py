"""
关于商品的统计

-[x] 所有的商品的品牌占比百分百饼图
-[ ] 库存中的品牌占比百分比饼图x2(本月和全部)
-[x] 所有卖出的品牌百分比饼图x2(本月和全部）
-[ ] 最近 30 天内各个品牌的售出情况
"""

from src.common.database.controller.chart_plugin_controller import ChartPluginController
from src.common.plugins.chart_plugins.chart.chart_base import NoContentHTML
from src.common.plugins.chart_plugins.chart.pie_chart import PieChart
from src.common.plugins.plugin_base import Chart, ChartSet
from src.enums import TimeFilterEnum


class BrandChart1(Chart):
    chart_title: str = "全部库存中各个品牌占比"
    chart_subtilte: str = "统计当前库存中所有的商品的品牌占比百分百饼图"

    def __init__(self):
        self._controller = ChartPluginController()

    def get_html(self) -> str:
        self._data = self._controller.get_count_groupby_brand()
        self._pie_chart = PieChart(self._data, self.chart_title, self.chart_subtilte)

        if self._data:
            return self._pie_chart.get_chart().render_embed()
        return NoContentHTML

    get_html.__doc__ = Chart.get_html.__doc__


class BrandChart2(Chart):
    chart_title = "本月库存中各个品牌占比"
    chart_subtilte = "统计当前库存中所有的商品的品牌占比百分百饼图"

    def __init__(self):
        self._controller = ChartPluginController()

    def get_html(self) -> str:
        self._data = self._controller.get_count_groupby_brand(
            statistic_time=TimeFilterEnum.Month
        )
        self._pie_chart = PieChart(self._data, self.chart_title, self.chart_subtilte)

        if self._data:
            return self._pie_chart.get_chart().render_embed()
        return NoContentHTML


class BrandChart3(Chart):
    chart_title = "过往售出商品中各个品牌占比"
    chart_subtilte = "统计过往全部卖出的商品的品牌占比百分百饼图"

    def __init__(self):
        self._controller = ChartPluginController()

    def get_html(self) -> str:
        self._data = self._controller.get_count_groupby_brand(
            is_sold=1, statistic_time=TimeFilterEnum.All
        )
        self._pie_chart = PieChart(self._data, self.chart_title, self.chart_subtilte)

        if self._data:
            return self._pie_chart.get_chart().render_embed()
        return NoContentHTML


class BrandChart4(Chart):
    chart_title = "本月售出商品中各个品牌占比"
    chart_subtilte = "统计本月卖出的商品的品牌占比百分百饼图"

    def __init__(self):
        self._controller = ChartPluginController()

    def get_html(self) -> str:
        self._data = self._controller.get_count_groupby_brand(
            is_sold=1, statistic_time=TimeFilterEnum.Month
        )
        self._pie_chart = PieChart(self._data, self.chart_title, self.chart_subtilte)

        if self._data:
            return self._pie_chart.get_chart().render_embed()
        return NoContentHTML


class BrandChartSet(ChartSet):
    """用于存放所有的品牌统计图"""

    plugin_name: str = "商品相关数据的统计"

    def _initialize(self) -> None:
        self.chart_list.append(BrandChart1())
        self.chart_list.append(BrandChart2())
        self.chart_list.append(BrandChart3())
        self.chart_list.append(BrandChart4())

    def get_description(self) -> str:
        return "这里是品牌相关数据的统计, 这里会从多个角度展示品牌的数据"
