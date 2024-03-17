from typing import List, Optional, Tuple

from pyecharts.charts import Pie
from pyecharts.options import (
    InitOpts,
    LabelOpts,
    LegendOpts,
    TitleOpts,
    ToolBoxFeatureDataViewOpts,
    ToolBoxFeatureDataZoomOpts,
    ToolBoxFeatureMagicTypeOpts,
    ToolBoxFeatureOpts,
    ToolBoxFeatureRestoreOpts,
    ToolboxOpts,
)

from src.common.plugins.chart_plugins.chart.chart_base import PyEChartsBase


class PieChart(PyEChartsBase):
    def __init__(
        self,
        data: List[Tuple[str, int]],
        chart_title: Optional[str] = None,
        chart_subtitle: Optional[str] = None,
    ):
        super().__init__()
        self._data = data
        self.chart = Pie(
            init_opts=InitOpts(theme=self.echarts_theme, width="100%", height="440px")
        )
        if self._data:
            self._create_chart(chart_title, chart_subtitle)

    def get_chart(self) -> Pie:
        return self.chart

    def _create_chart(
        self, chart_title: Optional[str] = None, chart_subtitle: Optional[str] = None
    ) -> Pie:
        tool_box_feature_magic_type_opts = ToolBoxFeatureMagicTypeOpts(is_show=False)
        tool_box_feature_opts = ToolBoxFeatureOpts(
            magic_type=tool_box_feature_magic_type_opts,
            data_view=ToolBoxFeatureDataViewOpts(is_show=False),
            data_zoom=ToolBoxFeatureDataZoomOpts(is_show=False),
            restore=ToolBoxFeatureRestoreOpts(is_show=False),
        )

        self.chart.add(
            series_name="详细信息",
            data_pair=self._data,
            selected_mode=True,
            rosetype="redius",
        )

        self.chart.set_global_opts(
            title_opts=TitleOpts(title=chart_title, subtitle=chart_subtitle),
            legend_opts=LegendOpts(type_="scroll", pos_left="85%", orient="vertical"),
            toolbox_opts=ToolboxOpts(feature=tool_box_feature_opts),
        )

        self.chart.set_series_opts(
            center=["40%", "50%"],
            radius=["50%", "70%"],
            label_opts=LabelOpts(
                formatter="{a|{a}}{abg|}\n{hr|}\n {b|{b}: }{c}件  {per|{d}%}  ",
                rich={
                    "a": {"color": "#999", "lineHeight": 22, "align": "center"},
                    "abg": {
                        "backgroundColor": "#e3e3e3",
                        "width": "100%",
                        "align": "right",
                        "height": 22,
                        "borderRadius": [4, 4, 0, 0],
                    },
                    "hr": {
                        "borderColor": "#aaa",
                        "width": "100%",
                        "borderWidth": 0.5,
                        "height": 0,
                    },
                    "b": {"fontSize": 16, "lineHeight": 33},
                    "per": {
                        "color": "#eee",
                        "backgroundColor": "#334455",
                        "padding": [2, 4],
                        "borderRadius": 2,
                    },
                },
                position="outside",
            ),
        )
        return self.chart


if __name__ == "__main__":
    from PySide6.QtWidgets import QApplication
    from PySide6.QtWebEngineWidgets import QWebEngineView

    app = QApplication([])
    web = QWebEngineView()
    p = PieChart(
        [("A", 10), ("B", 20), ("C", 30), ("D", 40), ("E", 50), ("F", 60)],
        "饼图",
        "这是子标题",
    )
    web.setHtml(p.get_chart().render_embed())
    web.resize(800, 600)
    web.show()
    app.exec()
