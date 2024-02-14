from PySide6.QtWidgets import QWidget
from typing_extensions import Self

from src.dict_typing import CustomBaseDict


class PluginBase:
    plugin_name: str = 'PluginBase'

    def __call__(self) -> Self:
        return self


class DatabasePluginBase(PluginBase):
    plugin_name: str = 'DatabasePluginBase'
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

    def get_description(self) -> str:
        """这里设置显示在表格上面对当前状态的描述"""
        raise NotImplementedError("需要实现这个方法")

    def get_custom_widget(self) -> QWidget:
        """这里返回自定义的widget,之后会被添加到表格上面的组件中"""
        raise NotImplementedError("需要实现这个方法")

    def _initialize(self) -> None:
        """这里设置一些初始化的操作,可以为空"""
        raise NotImplementedError("需要实现这个方法")

    def _connect_signals(self) -> None:
        """这里设置信号与槽的连接,如果没有自定义的widget,则不需要实现这个方法"""
        raise NotImplementedError("需要实现这个方法")
