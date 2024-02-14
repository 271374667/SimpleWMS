from typing import Optional

import loguru
from PySide6.QtWidgets import QApplication, QVBoxLayout

from src.common.plugins.plugin_base import DatabasePluginBase
from src.common.plugins.plugin_manager import DatabasePluginManager
from src.model.database_model import DatabaseModel
from src.table_handler import TableHandler
from src.view.database_view import DatabaseView


class DatabasePresenter:
    def __init__(self):
        self._view = DatabaseView()
        self._model = DatabaseModel()
        self._database_plugin_manager = DatabasePluginManager()
        self._table_handler = TableHandler(self._view.get_table())
        loguru.logger.debug(f'当前启用插件:{self._database_plugin_manager.get_all_plugins()}')

        # 初始化插件
        self._init_plugins()
        self._connect_signal()

    def get_view(self):
        return self._view

    def get_model(self):
        return self._model

    def _init_plugins(self):
        # 初始化插件
        plugins = self._database_plugin_manager.get_all_plugins()
        for plugin in plugins.values():
            self._view.get_plugin_select_comboBox().addItem(plugin.plugin_name, plugin.plugin_name)

        if len(plugins) == 0:
            self._view.show_error_infobar("插件初始化失败", "插件初始化失败,没有获取到任何插件", 10)
            return

        ui = self.get_view()
        combox_box = ui.get_plugin_select_comboBox()
        current_plugin: Optional[DatabasePluginBase] = self._database_plugin_manager.get_plugin_by_name(
                combox_box.currentText())
        if not current_plugin:
            self.get_view().show_error_infobar("插件初始化失败", f'插件{combox_box.currentText()}初始化失败', 10)
            return

        # 设置描述
        ui.get_description_label().setText(current_plugin.get_description())
        # 设置自定义widget
        custom_widget = ui.get_custom_widget()
        inner_layout = QVBoxLayout()
        inner_layout.addWidget(current_plugin.get_custom_widget())
        custom_widget.setLayout(inner_layout)

        # 设置表格
        self._table_handler.set_show_headers(current_plugin.table_show_headers)
        self._table_handler.set_headers(current_plugin.table_headers)

    def _plugin_changed(self) -> None:
        ui = self.get_view()
        combox_box = ui.get_plugin_select_comboBox()
        current_plugin: Optional[DatabasePluginBase] = self._database_plugin_manager.get_plugin_by_name(
                combox_box.currentText())
        if not current_plugin:
            self.get_view().show_error_infobar("插件初始化失败", f'插件{combox_box.currentText()}初始化失败', 10)
            return

        # 设置描述
        ui.get_description_label().setText(current_plugin.get_description())
        # 设置自定义widget
        custom_widget = ui.get_custom_widget()
        # 先清除之前custom_widget的所有内容
        for i in custom_widget.children():
            if i == custom_widget.layout():
                continue
            i.deleteLater()

        inner_layout = custom_widget.layout()
        inner_layout.addWidget(current_plugin.get_custom_widget())
        # print(custom_widget.layout())

        # 设置表格
        self._table_handler.set_show_headers(current_plugin.table_show_headers)
        self._table_handler.set_headers(current_plugin.table_headers)

    def _submit(self):
        self._table_handler.clear()
        current_plugin: Optional[DatabasePluginBase] = self._database_plugin_manager.get_plugin_by_name(
                self._view.get_plugin_select_comboBox().currentText())
        if not current_plugin:
            self.get_view().show_error_infobar("插件初始化失败",
                                               f'插件{self._view.get_plugin_select_comboBox().currentText()}初始化失败',
                                               10)
            return
        self._table_handler.set_data(current_plugin.get_data())
        self._table_handler.scroll_to_row(0)

    def _connect_signal(self) -> None:
        ui = self.get_view()
        submit_btn = ui.get_submit_button()
        submit_btn.clicked.connect(self._submit)
        ui.get_plugin_select_comboBox().currentIndexChanged.connect(self._plugin_changed)


if __name__ == "__main__":
    app = QApplication([])
    database_presenter = DatabasePresenter()
    database_presenter.get_view().show()
    app.exec()
