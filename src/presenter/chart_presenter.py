import loguru

from src.common.plugins.plugin_manager import ChartPluginManager
from src.model.chart_model import ChartModel
from src.view.chart_view import ChartView


class ChartPresenter:
    def __init__(self):
        self._view = ChartView()
        self._model = ChartModel()
        self._chart_plugin_manager = ChartPluginManager()
        loguru.logger.debug(f'当前启用插件:{self._chart_plugin_manager.get_all_plugins()}')

        # 初始化插件
        self._init_plugins()
        self._connect_signal()

    def get_view(self) -> ChartView:
        return self._view

    def get_model(self) -> ChartModel:
        return self._model

    def _init_plugins(self) -> None:
        # 初始化插件
        plugins = self._chart_plugin_manager.get_all_plugins()
        for plugin in plugins.values():
            self._view.get_plugin_select_comboBox().addItem(plugin.plugin_name, plugin.plugin_name)

            # 设置每一个图表
            for each in plugin.chart_list:
                self._view.get_chart_select_comboBox().addItem(each.chart_title)

        if len(plugins) == 0:
            self._view.show_error_infobar("插件初始化失败", "插件初始化失败,没有获取到任何插件", 10)
            return

        ui = self.get_view()
        combox_box = ui.get_plugin_select_comboBox()
        current_plugin = self._chart_plugin_manager.get_plugin_by_name(combox_box.currentText())
        if not current_plugin:
            self.get_view().show_error_infobar("插件初始化失败", f'插件{combox_box.currentText()}初始化失败', 10)
            return

        # 设置描述
        ui.get_description_label().setText(current_plugin.get_description())

        # 设置图表
        current_chart_index = self._view.get_chart_select_comboBox().currentIndex()
        self._view.get_web_view().setHtml(current_plugin.get_html(current_chart_index))

    def _submit(self) -> None:
        ui = self.get_view()
        combox_box = ui.get_plugin_select_comboBox()
        current_plugin = self._chart_plugin_manager.get_plugin_by_name(combox_box.currentText())
        if not current_plugin:
            self.get_view().show_error_infobar("插件初始化失败", f'插件{combox_box.currentText()}初始化失败', 10)
            return

        # 设置描述
        ui.get_description_label().setText(current_plugin.get_description())

        # 设置图表
        current_chart_index = self._view.get_chart_select_comboBox().currentIndex()
        self._view.get_web_view().setHtml(current_plugin.get_html(current_chart_index))

    def _connect_signal(self) -> None:
        self._view.get_submit_button().clicked.connect(self._submit)


if __name__ == '__main__':
    from PySide6.QtWidgets import QApplication

    app = QApplication([])
    presenter = ChartPresenter()
    presenter.get_view().show()
    app.exec()
