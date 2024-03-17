from PySide6.QtCore import QObject
from pyecharts.charts.chart import Chart
from pyecharts.globals import ThemeType


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


NoContentHTML = """
<!DOCTYPE html>
<html lang="zh-CN">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>无数据提示</title>
  <style>
    * {
      margin: 0;
      padding: 0;
    }

    section {
      width: 100%;
      height: 100vh;
      display: flex;
      justify-content: center;
      align-items: center;
    }

    .message {
      color: black;
      font-size: 24px;
    }

    */
  </style>
</head>

<body>
  <section>
    <div class="message">当前图表没有任何数据</div>

  </section>
</body>

</html>
"""
