import subprocess
import sys
from PySide6.QtWidgets import QApplication

import loguru

from src.config import cfg
from src.constant import DATABASE_FILE


class SettingModel:
    def __init__(self):
        self._cfg = cfg

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
