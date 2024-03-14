import os
from pathlib import Path

import loguru
import pandas as pd

from src.common.database.controller.setting_controller import SettingController
from src.config import cfg


class SettingModel:
    def __init__(self):
        self._cfg = cfg
        self._seing_controller = SettingController()

    def set_backup_path(self, path: str) -> None:
        self._cfg.set(cfg.backup_path, path)

    def set_retrieval_path(self, path: str) -> None:
        self._cfg.set(cfg.retrieval_path, path)

    def set_storage_path(self, path: str) -> None:
        self._cfg.set(cfg.storage_path, path)

    def set_font(self, font: str) -> None:
        self._cfg.set(cfg.font, font)

    def set_log_rotation_days(self, days: int) -> None:
        self._cfg.set(cfg.log_rotation_days, days)

    def set_log_retention_days(self, days: int) -> None:
        self._cfg.set(cfg.log_retention_days, days)

    def set_email_account(self, account: str) -> None:
        self._cfg.set(cfg.email_account, account)

    def set_email_secret_key(self, secret_key: str) -> None:
        self._cfg.set(cfg.email_secret_key, secret_key)

    def export_database(self, path: Path) -> None:
        """导出数据库"""
        data = self._seing_controller.export_database()

        df = pd.DataFrame(data)
        loguru.logger.debug(f'一共有{len(df)}条数据')

        df.to_excel(path, index=False)
        loguru.logger.debug(f'导出数据库到{path}完成')

        # 打开保存的文件夹
        os.startfile(path.parent)
