import importlib
from pathlib import Path
from typing import Optional

from src.common.plugins.plugin_base import PluginBase
from src.constant import DATABASE_PLUGINS_DIR


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
    plugins_dir = DATABASE_PLUGINS_DIR


if __name__ == '__main__':
    print(DatabasePluginManager.get_all_plugins())
