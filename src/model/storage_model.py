import os
from dataclasses import asdict
from datetime import datetime
from pathlib import Path
from typing import Tuple

import loguru
import pandas as pd

from src.common.database.controller.storage_controller import StorageController
from src.common.database.utils import convert
from src.config import cfg


class StorageModel:
    def __init__(self):
        self._db_controller = StorageController()

    def get_newest_batch_serial_number(self) -> str:
        """获取最新的批次"""
        return self._db_controller.get_latest_batch_serial_number()

    def get_newest_batch_number(self) -> int:
        """获取最新的批次序号"""
        return int(self.get_newest_batch_serial_number()[-3:])

    def gen_batch_serial_number(self, number: int) -> str:
        """根据传入的数据生成批次号

        年月为当前年月,序号为传入的数字
        例如传入 1，那么就会生成 202401001
        例如传入 2，那么就会生成 202401002
        例如传入 15，那么就会生成 202401015
        Args:
            number: 传入的数字

        """
        today = datetime.today()
        return f'{today.year}{today.month:02d}{number:03d}'

    def export_data(self, data: list[Tuple[str, str, float, str]]) -> None:
        """导出数据到Excel和数据库"""
        # 先获取最新的inventory_id
        latest_inventory_id = self._db_controller.get_latest_inventory_id()

        # 要先导出到数据库才能获取到id和EAN13
        self._db_controller.export_to_database(data)

        new_data = self._db_controller.get_all_inventory_and_batch_greater_than_id(latest_inventory_id)
        print(new_data)
        # 将数据类对象转换为字典列表
        dict_list = [asdict(item) for item in new_data]

        # 创建一个DataFrame
        df = pd.DataFrame(dict_list)

        # 重新排序列以匹配所需的顺序
        df = df[['item_id', 'item_name', 'brand', 'price', 'batch_name', 'batch_serial_number', 'created_time']]

        # 对其中的item_id列全部调用函数转换成EAN13
        df['item_id'] = df['item_id'].apply(convert.convert_id_to_ean13)

        # 重命名列以匹配所需的标题
        df.columns = ['EAN13', '名称', '品牌', '价格', '批次名', '批次序号', '批次创建时间']

        # 将DataFrame导出为Excel文件
        save_dir = Path(cfg.get(cfg.storage_path))
        EXCEL_FILE = save_dir / f'入库信息{datetime.today().strftime("%Y-%m-%d-%H-%M-%S")}.xlsx'
        df.to_excel(EXCEL_FILE, index=False)
        loguru.logger.debug(f'导出数据到Excel文件:{EXCEL_FILE}')
        loguru.logger.debug(f'本次导出了{len(dict_list)}条数据到Excel文件')
        os.startfile(save_dir)


if __name__ == "__main__":
    s = StorageModel()
