import os
from pathlib import Path
from typing import List

import loguru
import pandas as pd
from PySide6.QtCore import Signal

from src.common.database.controller.setting_controller import SettingController
from src.common.database.utils import convert
from src.config import cfg
from src.dict_typing import AllInventoryDict


class SettingModel:
    def __init__(self):
        self._cfg = cfg
        self._setting_controller = SettingController()

    def get_progress_signal(self) -> Signal:
        return self._setting_controller.import_database_progress

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

    def export_database(self, file_path: Path) -> None:
        """导出数据库"""
        data = self._setting_controller.export_database()

        df = pd.DataFrame(data)
        loguru.logger.debug(f'一共有{len(df)}条数据')

        df.to_excel(file_path, index=False)
        loguru.logger.debug(f'导出数据库到{file_path}完成')

        # 打开保存的文件夹
        os.startfile(file_path.parent)

    def import_database(self, file_path: Path) -> None:
        """导入数据库"""
        # TODO: 当前的数据库非常耗时,需要优化
        result = pd.read_excel(file_path)
        loguru.logger.debug(f'一共有{len(result)}条数据')
        # 将所有的ean13从id转换成ean13
        result['ean13'] = result['ean13'].apply(convert.EAN13Converter.convert_id_to_ean13)

        data: List[AllInventoryDict] = result.to_dict(orient='records')
        # 把所有的nan转换成None,同时把timestamp转换成datetime
        for item in data:
            for key, value in item.items():
                if pd.isna(value):
                    item[key] = None
                elif isinstance(value, pd.Timestamp):
                    item[key] = value.to_pydatetime()

        self._setting_controller.import_database(data)
        loguru.logger.debug(f'导入数据库完成')

    def clear_database(self) -> None:
        """清空数据库"""
        self._setting_controller.clear_database()


if __name__ == '__main__':
    s = SettingModel()
    # s.export_database(Path(r'E:\load\即将删除\文档\一些测试\新建文件夹\新建文件夹1.xlsx'))
    s.import_database(Path(r'E:\load\即将删除\文档\一些测试\新建文件夹\新建文件夹1.xlsx'))
