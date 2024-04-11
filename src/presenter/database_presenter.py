from typing import Optional

import loguru
from PySide6.QtWidgets import QApplication, QFileDialog, QVBoxLayout

from src.common.plugins.plugin_base import DatabasePluginBase
from src.common.plugins.plugin_manager import DatabasePluginManager
from src.core.wms_dataclass import DataclassBase
from src.model.database_model import DatabaseModel
from src.utils.run_in_thread import RunInThread
from src.view.database_view import DatabaseView
from src.utils.excel_handler import ExcelHandler


class DatabasePresenter:
    def __init__(self):
        self._view = DatabaseView()
        self._model = DatabaseModel()
        self._database_plugin_manager = DatabasePluginManager()
        self._excel_handler = ExcelHandler()
        loguru.logger.debug(
            f"当前启用插件:{self._database_plugin_manager.get_all_plugins()}"
        )

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
            self._view.get_plugin_select_comboBox().addItem(
                plugin.plugin_name, plugin.plugin_name
            )

        if len(plugins) == 0:
            self._view.show_error_infobar(
                "插件初始化失败", "插件初始化失败,没有获取到任何插件", 10
            )
            return

        ui = self.get_view()
        combox_box = ui.get_plugin_select_comboBox()
        current_plugin: Optional[DatabasePluginBase] = (
            self._database_plugin_manager.get_plugin_by_name(combox_box.currentText())
        )
        if not current_plugin:
            self.get_view().show_error_infobar(
                "插件初始化失败", f"插件{combox_box.currentText()}初始化失败", 10
            )
            return

        # 设置描述
        ui.get_description_label().setText(current_plugin.get_description())
        # 设置自定义widget
        custom_widget = ui.get_custom_widget()
        inner_layout = QVBoxLayout()
        inner_layout.addWidget(current_plugin.get_custom_widget())
        custom_widget.setLayout(inner_layout)

        # 设置表格
        self.get_view().get_table().set_dataclass(current_plugin.table_dataclass)
        self._excel_handler.set_dataclass(current_plugin.table_dataclass)

    def _plugin_changed(self) -> None:
        ui = self.get_view()
        combox_box = ui.get_plugin_select_comboBox()
        current_plugin: Optional[DatabasePluginBase] = (
            self._database_plugin_manager.get_plugin_by_name(combox_box.currentText())
        )
        if not current_plugin:
            self.get_view().show_error_infobar(
                "插件初始化失败", f"插件{combox_box.currentText()}初始化失败", 10
            )
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

        # 设置表格
        self.get_view().get_table().set_dataclass(current_plugin.table_dataclass)
        self._excel_handler.set_dataclass(current_plugin.table_dataclass)

    def _submit(self):
        self.get_view().get_table().clear()
        current_plugin: Optional[DatabasePluginBase] = (
            self._database_plugin_manager.get_plugin_by_name(
                self._view.get_plugin_select_comboBox().currentText()
            )
        )
        if not current_plugin:
            self.get_view().show_error_infobar(
                "插件初始化失败",
                f"插件{self._view.get_plugin_select_comboBox().currentText()}初始化失败",
                10,
            )
            return

        self.get_view().show_state_tooltip("正在获取数据...", "正在从数据库获取数据")
        self.run_in_thread = RunInThread()

        def run() -> list[DataclassBase]:
            return current_plugin.get_data()

        def finish(data: list[DataclassBase]) -> None:
            self.get_view().get_table().set_data(data)
            self.get_view().get_table().get_table().scrollToTop()
            self.get_view().finish_state_tooltip("成功", "数据获取成功")

        self.run_in_thread.set_start_func(run)
        self.run_in_thread.set_finished_func(finish)
        self.run_in_thread.start()

    def _reflesh(self) -> None:
        self.get_view().show_success_infobar(
            "刷新成功", "所有的数据已经重新从数据库获取", 3000
        )
        self._submit()

    def _export_table(self) -> None:
        self._run_in_thread = RunInThread()

        file_path, _ = QFileDialog.getSaveFileName(
            self.get_view(), "保存文件", "", "Excel Files (*.xlsx)"
        )
        if not file_path:
            return

        loguru.logger.debug(f"当前选择的文件路径为{file_path}")
        self.get_view().show_state_tooltip(
            "正在导出数据...", f"正在导出数据到{file_path}"
        )

        def run():
            self._excel_handler.set_data(self.get_view().get_table().get_all_data())
            self._excel_handler.export2excel(file_path)

        def finish() -> None:
            self.get_view().finish_state_tooltip(
                "成功", f"数据已经成功导出到{file_path[0]}"
            )

        self._run_in_thread.set_start_func(run)
        self._run_in_thread.set_finished_func(finish)
        self._run_in_thread.start()

    def _connect_signal(self) -> None:
        ui = self.get_view()
        submit_btn = ui.get_submit_button()
        submit_btn.clicked.connect(self._submit)
        ui.get_plugin_select_comboBox().currentIndexChanged.connect(
            self._plugin_changed
        )
        ui.get_refresh_action().triggered.connect(self._reflesh)
        ui.get_export_action().triggered.connect(self._export_table)


if __name__ == "__main__":
    app = QApplication([])
    database_presenter = DatabasePresenter()
    database_presenter.get_view().show()
    app.exec()
