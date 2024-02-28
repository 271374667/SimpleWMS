from datetime import date, timedelta
from typing import List, Optional, Sequence, Tuple, Union

from pyecharts.charts import Bar
from pyecharts.charts.chart import Chart
from pyecharts.options import (AxisOpts, DataZoomOpts, InitOpts, LabelOpts, MarkPointItem,
                               MarkPointOpts, TitleOpts, ToolBoxFeatureDataViewOpts, ToolBoxFeatureMagicTypeOpts,
                               ToolBoxFeatureOpts, ToolboxOpts, TooltipOpts)

from src.common.plugins.chart_plugins.chart.chart_base import PyEChartsBase


class BarChart(PyEChartsBase):
    def __init__(self, data: List[Tuple[str, Sequence]],
                 chart_title: Optional[str] = None,
                 chart_subtitle: Optional[str] = None,
                 xaxis_labels: Optional[List[Union[date, str]]] = None
                 ):
        super().__init__()
        self.chart = Bar(init_opts=InitOpts(theme=self.echarts_theme, width="100%", height='440px'))

        tool_box_feature_magic_type_opts = ToolBoxFeatureMagicTypeOpts(
                type_=["stack", "tiled"],
                )
        tool_box_feature_opts = ToolBoxFeatureOpts(
                magic_type=tool_box_feature_magic_type_opts,
                data_view=ToolBoxFeatureDataViewOpts(is_show=False),
                )

        # 设置 x 轴标签(默认是时间)
        if xaxis_labels:
            self.chart.add_xaxis(xaxis_labels)
        else:
            # 如果没有设置x轴标签,则自动生成日期标签
            max_length = max(len(d[1]) for d in data)
            x_data = [date.today() - timedelta(days=max_length - i) for i in range(max_length)]
            self.chart.add_xaxis(x_data)

        for name, values in data:
            self.chart.add_yaxis(series_name=name,
                                 y_axis=values,
                                 markpoint_opts=MarkPointOpts(
                                         data=[
                                                 MarkPointItem(type_="max", name="最大值"),
                                                 MarkPointItem(type_="min", name="最小值"),
                                                 ]
                                         )
                                 )

        self.chart.set_global_opts(
                title_opts=TitleOpts(title=chart_title, subtitle=chart_subtitle),
                xaxis_opts=AxisOpts(axislabel_opts=LabelOpts(rotate=-15), name="日期"),
                datazoom_opts=[DataZoomOpts(range_start=0, range_end=100), DataZoomOpts(type_="inside")],
                yaxis_opts=AxisOpts(axislabel_opts=LabelOpts(formatter="{value} 件"), name="数量"),
                toolbox_opts=ToolboxOpts(feature=tool_box_feature_opts),
                tooltip_opts=TooltipOpts(trigger="axis", axis_pointer_type="cross"),
                )

        self.chart.set_series_opts(
                label_opts=LabelOpts(is_show=True),
                )

    def get_chart(self) -> Chart:
        return self.chart


if __name__ == '__main__':
    from PySide6.QtWidgets import QApplication
    from PySide6.QtWebEngineWidgets import QWebEngineView
    from random import randint

    data = [("A", [randint(1, 100) for _ in range(10)]),
            ("B", [randint(1, 100) for _ in range(10)]),
            ("C", [randint(1, 100) for _ in range(10)]),
            ("D", [randint(1, 100) for _ in range(10)]),
            ("E", [randint(1, 100) for _ in range(10)]),
            ]

    app = QApplication([])
    web = QWebEngineView()
    b = BarChart(data, chart_title='主标题', chart_subtitle='子标题')
    web.setHtml(b.get_chart().render_embed())
    web.resize(800, 600)
    web.show()
    app.exec()
