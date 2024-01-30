from src.config import cfg


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
