from datetime import date, timedelta
from typing import List, Tuple, Union

from pyecharts.charts import Line
from pyecharts.options import (AxisOpts, DataZoomOpts, InitOpts, LabelOpts, MarkLineItem, MarkLineOpts, MarkPointItem,
                               MarkPointOpts,
                               TitleOpts, ToolBoxFeatureDataViewOpts, ToolBoxFeatureMagicTypeOpts, ToolBoxFeatureOpts,
                               ToolboxOpts)

from src.common.plugins.chart_plugins.chart.chart_base import PyEChartsBase


class LineChart(PyEChartsBase):
    def __init__(self):
        super().__init__()
        self.chart = Line(init_opts=InitOpts(theme=self.echarts_theme, width="100%"))

        self._tool_box_feature_magic_type_opts = ToolBoxFeatureMagicTypeOpts(
                type_=["stack", "tiled"],
                )
        self._tool_box_feature_opts = ToolBoxFeatureOpts(
                magic_type=self._tool_box_feature_magic_type_opts,
                data_view=ToolBoxFeatureDataViewOpts(is_show=False),
                )

    def set_title(self, title: str):
        self.chart.set_global_opts(title_opts=TitleOpts(title=title))

    def set_subtitle(self, subtitle: str):
        self.chart.set_global_opts(title_opts=TitleOpts(subtitle=subtitle))

    def set_data(self, data: List[Tuple[str, List[int]]], xaxis_labels: List[Union[date, str]] = None):
        self._data = data

        if xaxis_labels:
            self.chart.add_xaxis(xaxis_labels)
        else:
            # 如果没有设置x轴标签,则自动生成日期标签
            max_length = max(len(d[1]) for d in data)
            x_data = [date.today() - timedelta(days=max_length - i) for i in range(max_length)]
            self.chart.add_xaxis(x_data)

        for name, values in self._data:
            self.chart.add_yaxis(series_name=name,
                                 y_axis=values,
                                 is_smooth=True,
                                 markpoint_opts=MarkPointOpts(
                                         data=[
                                                 MarkPointItem(type_="max", name="最大值"),
                                                 MarkPointItem(type_="min", name="最小值"),
                                                 ]
                                         ),
                                 markline_opts=MarkLineOpts(
                                         data=[
                                                 MarkLineItem(type_="average", name="平均值"),
                                                 ]
                                         ),
                                 )

        self.chart.set_global_opts(
                title_opts=TitleOpts(title="Line-基本示例", subtitle="我是副标题"),
                xaxis_opts=AxisOpts(axislabel_opts=LabelOpts(rotate=-15), name="日期"),
                datazoom_opts=[DataZoomOpts(), DataZoomOpts(type_="inside")],
                yaxis_opts=AxisOpts(axislabel_opts=LabelOpts(formatter="{value} 件"), name="数量"),
                toolbox_opts=ToolboxOpts(feature=self._tool_box_feature_opts),
                )

        self.chart.set_series_opts(
                label_opts=LabelOpts(is_show=True),
                )

    def set_xaxis_label(self, labels: List[str]):
        self.chart.add_xaxis(labels)

    def get_chart(self) -> Line:
        return self.chart


if __name__ == '__main__':
    from PySide6.QtWidgets import QApplication
    from PySide6.QtWebEngineWidgets import QWebEngineView
    from random import randint

    app = QApplication([])
    web = QWebEngineView()
    l = LineChart()
    l.set_title("Line-基本示例")
    l.set_subtitle("我是副标题")
    l.set_data([("A", [randint(0, 100) for _ in range(50)]), ("B", [randint(0, 100) for _ in range(100)])])
    # l.set_title('我是设置之后的标题')
    web.setHtml(l.get_chart().render_embed())
    web.resize(800, 600)
    web.show()
    app.exec()
