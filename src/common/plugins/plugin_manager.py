import importlib
from pathlib import Path
from typing import Optional

from src.common.plugins.database_plugins.out_of_stock_plugin import OutOfStockPlugin
from src.common.plugins.database_plugins.return_times_plugin import ReturnTimesPlugin
from src.common.plugins.database_plugins.unsalable_plugin import UnsalablePlugin
from src.common.plugins.plugin_base import PluginBase


class PluginManagerBase:
    plugins: dict[str, PluginBase] = {}
    plugins_dir: Optional[Path] = None

    def __init__(self):
        if self.plugins_dir is not None:
            self._load_plugins()

    def _load_plugins(self):
        for each in self.plugins_dir.iterdir():
            if each.is_file() and each.suffix == '.py':
                importlib.import_module(f'src.common.plugins.{self.plugins_dir.name}.{each.stem}')

    @classmethod
    def register(cls, plugin: PluginBase):
        if plugin.plugin_name in cls.plugins:
            return

        cls.plugins[plugin.plugin_name] = plugin()
        return plugin

    @classmethod
    def get_all_plugins(cls) -> dict[str, PluginBase]:
        return cls.plugins

    @classmethod
    def get_plugin_by_name(cls, name: str) -> Optional[PluginBase]:
        return cls.plugins.get(name)


class DatabasePluginManager(PluginManagerBase):
    def __init__(self):
        super().__init__()
        # 为了让pyinstaller能够识别，所以还是用了实例化的方法

        self.plugins.setdefault(UnsalablePlugin.plugin_name, UnsalablePlugin())
        self.plugins.setdefault(OutOfStockPlugin.plugin_name, OutOfStockPlugin())
        self.plugins.setdefault(ReturnTimesPlugin.plugin_name, ReturnTimesPlugin())


if __name__ == '__main__':
    print(DatabasePluginManager.get_all_plugins())
