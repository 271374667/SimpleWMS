from typing import Optional

import loguru
from PySide6.QtWidgets import QWidget
from typing_extensions import Self

from src.core.dict_typing import CustomBaseDict


class PluginBase:
    plugin_name: str = "PluginBase"
    has_initialize: bool = True

    def __call__(self) -> Self:
        return self

    def get_description(self) -> str:
        """这里设置显示在表格上面对当前状态的描述"""
        raise NotImplementedError("需要实现这个方法")

    def _initialize(self) -> None:
        """这里设置一些初始化的操作,可以为空"""
        raise NotImplementedError("需要实现这个方法")


class DatabasePluginBase(PluginBase):
    plugin_name: str = "DatabasePluginBase"
    has_custom_widget: bool = True
    has_initialize: bool = True
    table_show_headers: list[str] = []
    table_headers: CustomBaseDict

    def __init__(self):
        super().__init__()
        if self.has_initialize:
            self._initialize()

        if self.has_custom_widget:
            self._connect_signals()

    def get_data(self) -> list[CustomBaseDict]:
        """从数据库中获取数据,以供表格显示"""
        raise NotImplementedError("需要实现这个方法")

    def get_custom_widget(self) -> QWidget:
        """这里返回自定义的widget,之后会被添加到表格上面的组件中"""
        raise NotImplementedError("需要实现这个方法")

    def _connect_signals(self) -> None:
        """这里设置信号与槽的连接,如果没有自定义的widget,则不需要实现这个方法"""
        raise NotImplementedError("需要实现这个方法")

    def get_description(self) -> str:
        """这里设置显示在表格上面对当前状态的描述"""
        raise NotImplementedError("需要实现这个方法")

    def _initialize(self) -> None:
        """这里设置一些初始化的操作,可以为空"""
        raise NotImplementedError("需要实现这个方法")


class Chart:
    """具体的图表"""

    chart_title: str = "chart_title"
    chart_subtilte: str = "chart_subtilte"

    def get_html(self) -> str:
        """获取图表的 html"""
        raise NotImplementedError("请在子类中实现该方法")


class ChartSet(PluginBase):
    """图表集合,负责存储上面的Chart"""

    plugin_name: str = ""
    chart_list: list[Chart] = []
    has_initialize: bool = True

    def __init__(self):
        super().__init__()
        if self.has_initialize:
            self._initialize()

    def get_html(self, index: int) -> Optional[str]:
        """获取图表"""
        try:
            return self.chart_list[index].get_html()
        except IndexError:
            loguru.logger.error(f"当前图表索引{index}超出范围")
            return None

    def get_description(self) -> str:
        """这里设置显示在表格上面对当前状态的描述"""
        raise NotImplementedError("需要实现这个方法")

    def _initialize(self) -> None:
        """这里设置一些初始化的操作,可以为空"""
        raise NotImplementedError("需要实现这个方法")
