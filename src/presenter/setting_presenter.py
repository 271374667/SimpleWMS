from PySide6.QtWidgets import QFileDialog

from src.model.setting_model import SettingModel
from src.view.setting_view import SettingView


class SettingPresenter:
    def __init__(self):
        self._view = SettingView()
        self._model = SettingModel()
        self._connect_singal()

    def get_view(self) -> SettingView:
        return self._view

    def get_model(self) -> SettingModel:
        return self._model

    def _backup_path_card_clicked(self) -> None:
        path = QFileDialog.getExistingDirectory(self.get_view(), "选择一个文件夹来保存备份")
        if path:
            self.get_view().backup_path_card.setContent(path)
            self.get_model().set_backup_path(path)
            self.get_view().show_success_infobar("设置成功", f'备份路径已经设置为{path}', duration=5000)

    def _retrieval_path_card_clicked(self) -> None:
        path = QFileDialog.getExistingDirectory(self.get_view(), "选择一个文件夹来保存备份")
        if path:
            self.get_view().retrieval_path_card.setContent(path)
            self.get_model().set_retrieval_path(path)
            self.get_view().show_success_infobar("设置成功", f'出库文件保存路径已经设置为{path}', duration=5000)

    def _storage_path_card_clicked(self) -> None:
        path = QFileDialog.getExistingDirectory(self.get_view(), "选择一个文件夹来保存入库的excel文件")
        if path:
            self.get_view().storage_path_card.setContent(path)
            self.get_model().set_storage_path(path)
            self.get_view().show_success_infobar("设置成功", f'入库文件保存路径已经设置为{path}', duration=5000)

    def _font_card_value_changed(self, value: str) -> None:
        self.get_model().set_font(value)
        self.get_view().show_success_infobar("设置成功", f'字体已经设置', duration=5000)

    def _log_rotation_days_card_value_changed(self, value: int) -> None:
        self.get_model().set_log_rotation_days(value)
        self.get_view().show_success_infobar("设置成功", f'日志归档天数已经设置为{value}', duration=5000)

    def _log_retention_days_card_value_changed(self, value: int) -> None:
        self.get_model().set_log_retention_days(value)
        self.get_view().show_success_infobar("设置成功", f'日志保留天数已经设置为{value}', duration=5000)

    def _connect_singal(self) -> None:
        ui = self.get_view()
        ui.backup_path_card.clicked.connect(self._backup_path_card_clicked)
        ui.retrieval_path_card.clicked.connect(self._retrieval_path_card_clicked)
        ui.storage_path_card.clicked.connect(self._storage_path_card_clicked)
        ui.font_card.optionChanged.connect(self._font_card_value_changed)
        ui.log_rotation_days_card.valueChanged.connect(self._log_rotation_days_card_value_changed)
        ui.log_retention_days_card.valueChanged.connect(self._log_retention_days_card_value_changed)
