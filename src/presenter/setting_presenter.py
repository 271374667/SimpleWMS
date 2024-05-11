from pathlib import Path

import loguru
from PySide6.QtWidgets import QFileDialog

from src.component.email_setting_component import EmailSettingComponent
from src.component.user_manager_component import UserManagerComponent
from src.model.setting_model import SettingModel
from src.utils.run_in_thread import RunInThread
from src.view.setting_view import SettingView


class SettingPresenter:
    def __init__(self):
        self._view = SettingView()
        self._model = SettingModel()
        self._user_manager_component = UserManagerComponent()
        self._connect_singal()

    def get_view(self) -> SettingView:
        return self._view

    def get_model(self) -> SettingModel:
        return self._model

    def _backup_path_card_clicked(self) -> None:
        if path := QFileDialog.getExistingDirectory(
            self.get_view(), "选择一个文件夹来保存备份"
        ):
            self.get_view().backup_path_card.setContent(path)
            self.get_model().set_backup_path(path)
            self.get_view().show_success_infobar(
                "设置成功", f"备份路径已经设置为{path}", duration=5000
            )

    def _retrieval_path_card_clicked(self) -> None:
        if path := QFileDialog.getExistingDirectory(
            self.get_view(), "选择一个文件夹来保存备份"
        ):
            self.get_view().retrieval_path_card.setContent(path)
            self.get_model().set_retrieval_path(path)
            self.get_view().show_success_infobar(
                "设置成功", f"出库文件保存路径已经设置为{path}", duration=5000
            )

    def _storage_path_card_clicked(self) -> None:
        if path := QFileDialog.getExistingDirectory(
            self.get_view(), "选择一个文件夹来保存入库的excel文件"
        ):
            self.get_view().storage_path_card.setContent(path)
            self.get_model().set_storage_path(path)
            self.get_view().show_success_infobar(
                "设置成功", f"入库文件保存路径已经设置为{path}", duration=5000
            )

    def _font_card_value_changed(self, value: str) -> None:
        self.get_model().set_font(value)
        self.get_view().show_success_infobar("设置成功", "字体已经设置", duration=5000)

    def _log_rotation_days_card_value_changed(self, value: int) -> None:
        self.get_model().set_log_rotation_days(value)

    def _log_retention_days_card_value_changed(self, value: int) -> None:
        self.get_model().set_log_retention_days(value)

    def _email_setting_component_clicked(self) -> None:
        email_setting_window = EmailSettingComponent(self.get_view())
        if not email_setting_window.exec():
            return

        account = email_setting_window.email_account.text()
        secret_key = email_setting_window.email_secret_key.text()
        self.get_model().set_email_account(account)
        self.get_model().set_email_secret_key(secret_key)
        loguru.logger.info(f"设置邮箱账号为{account}")

        self.get_view().show_success_infobar("设置成功", "邮箱设置成功", duration=5000)

    def _export_database_card_clicked(self) -> None:
        path = QFileDialog.getSaveFileName(
            self.get_view(), "导出数据库", "", "Excel Files (*.xlsx)"
        )[0]
        if not path:
            self.get_view().show_info_infobar(
                "导出取消", "您没有选择任何路径,已经取消导出数据库", duration=5000
            )
            return

        self.get_view().show_state_tooltip("导出数据库中……", f"正在导出数据到{path}")

        def run():
            self.get_model().export_database(Path(path))

        def finished():
            self.get_view().finish_state_tooltip()
            self.get_view().show_success_infobar(
                "导出成功", f"数据库已经导出到{path}", duration=5000
            )
            loguru.logger.success(f"导出数据库到{path}成功")

        self._run_in_thread = RunInThread()
        self._run_in_thread.set_start_func(run)
        self._run_in_thread.set_finished_func(finished)
        self._run_in_thread.start()

    def _import_database_card_clicked(self) -> None:
        path = QFileDialog.getOpenFileName(
            self.get_view(), "导入数据库", "", "Excel Files (*.xlsx)"
        )[0]
        if not path:
            self.get_view().show_info_infobar(
                "导入取消", "您没有选择任何文件,已经取消导入数据库", duration=5000
            )
            return

        confirm = self.get_view().show_mask_dialog(
            "警告", "导入数据库会清空当前数据库,是否继续?"
        )
        if not confirm:
            self.get_view().show_info_infobar(
                "导入取消", "您取消了导入数据库", duration=5000
            )
            return

        self.get_view().show_state_tooltip("导入数据库中……", f"正在导入数据从{path}")
        self.get_view().get_progress_bar().setVal(0)

        def run():
            self.get_model().clear_database()
            self.get_model().import_database(Path(path))

        def finished():
            self.get_view().finish_state_tooltip()
            self.get_view().show_success_infobar(
                "导入成功", f"数据库已经导入从{path}", duration=5000
            )
            loguru.logger.success(f"导入数据库从{path}成功")
            self.get_view().get_progress_bar().setVal(100)

        self._run_in_thread = RunInThread()
        self._run_in_thread.set_start_func(run)
        self._run_in_thread.set_finished_func(finished)
        self._run_in_thread.start()

    def _connect_singal(self) -> None:
        ui = self.get_view()
        ui.backup_path_card.clicked.connect(self._backup_path_card_clicked)
        ui.retrieval_path_card.clicked.connect(self._retrieval_path_card_clicked)
        ui.storage_path_card.clicked.connect(self._storage_path_card_clicked)
        ui.font_card.optionChanged.connect(self._font_card_value_changed)
        ui.log_rotation_days_card.valueChanged.connect(
            self._log_rotation_days_card_value_changed
        )
        ui.log_retention_days_card.valueChanged.connect(
            self._log_retention_days_card_value_changed
        )
        ui.email_account_card.clicked.connect(
            lambda: self._email_setting_component_clicked()
        )
        ui.export_database_card.clicked.connect(self._export_database_card_clicked)
        ui.import_database_card.clicked.connect(self._import_database_card_clicked)

        ui.user_manager_card.clicked.connect(self._user_manager_component.show)

        # 绑定一下进度条信号
        self.get_model().get_progress_signal().connect(ui.get_progress_bar().setVal)


if __name__ == "__main__":
    from PySide6.QtWidgets import QApplication

    app = QApplication([])
    w = SettingPresenter().get_view()
    w.show()
    app.exec()
