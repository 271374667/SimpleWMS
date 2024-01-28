import os
from datetime import datetime
from pathlib import Path
from typing import List, Optional, Tuple

import loguru
import pandas as pd

from src.common.database.controller.retrieval_controller import RetrievalController, RetrievalData
from src.config import cfg


class RetrievalModel:
    def __init__(self):
        self._db_controller = RetrievalController()
        self.lastest_wave: Optional[str] = None

    def get_inventory_by_ean13(self, ean13: str) -> Optional[RetrievalData]:
        result = self._db_controller.get_inventory_by_ean13(ean13)
        if result is None:
            return None
        return result

    def is_inventory_sold(self, ean13: str) -> bool:
        return self._db_controller.is_inventory_sold(ean13)

    def is_real_ean13(self, ean13: str) -> bool:
        """检测是否是真实的EAN13"""
        return self._db_controller.is_real_ean13(ean13)

    def get_wave_lastest_serial_number(self) -> str:
        # 使用缓存，如果缓存中没有，那么就从数据库中获取
        if self.lastest_wave is None:
            self.lastest_wave = self._db_controller.get_lastest_wave_serial_number()
        return self.lastest_wave

    def get_wave_lastest_number(self) -> int:
        # 使用缓存，如果缓存中没有，那么就从数据库中获取
        if self.lastest_wave is None:
            self.lastest_wave = self._db_controller.get_lastest_wave_serial_number()
        return int(self.lastest_wave[-3:])

    def get_lastest_wave_name(self) -> str:
        if self.lastest_wave is None:
            self.lastest_wave = self._db_controller.get_lastest_wave_serial_number()
        return self._db_controller.get_lastest_wave_serial_number()

    def export_data(self, data: List[Tuple[str, str, float, str, str, str]]) -> None:
        # 将原本的inventory里面的is_sold设置为1,然后新增一个Wave
        for each in data:
            # each = ['名称', '品牌', '价格', '波次名称', '入库时间', 'EAN13']
            self._db_controller.set_inventory_sold(each[-1], each[3])

        # 更新缓存
        self.lastest_wave = self._db_controller.get_lastest_wave_serial_number()

        # 将数据导出到xlsx文件
        # 将DataFrame导出为Excel文件

        df = pd.DataFrame({'名称': [each[0] for each in data],
                                  '品牌': [each[1] for each in data],
                                  '价格': [each[2] for each in data],
                                  '波次名称': [self._db_controller.convert_wave_serial_number_to_wave_name(each[3]) for
                                          each in data],
                                  '入库时间': [each[4] for each in data],
                                  'EAN13': [each[5] for each in data],
                                  })
        save_dir = Path(cfg.get(cfg.backup_path))
        EXCEL_FILE = save_dir / f'出库信息{datetime.today().strftime("%Y-%m-%d-%H-%M-%S")}.xlsx'
        df.to_excel(EXCEL_FILE, index=False)
        loguru.logger.debug(f'导出数据到Excel文件:{EXCEL_FILE}')
        loguru.logger.debug(f'本次导出了{len(df)}条数据到Excel文件')
        os.startfile(save_dir)
