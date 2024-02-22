import os
from dataclasses import asdict
from datetime import datetime
from pathlib import Path

import loguru
import pandas as pd

from src.common.database.controller.storage_controller import StorageController
from src.common.database.utils import convert
from src.config import cfg
from src.dict_typing import ReStorageDict, StorageCardDict


class StorageModel:
    def __init__(self):
        self._db_controller = StorageController()

    def get_inventory_by_ean13(self, ean13: str) -> ReStorageDict:
        """根据EAN13获取库存信息"""
        data = self._db_controller.get_inventory_by_ean13(ean13)
        row: ReStorageDict = {
                'name': str(data.item_name),
                'brand': str(data.brand),
                'price': float(data.price),
                'storage_time': data.batch.created_time,
                'return_times': int(data.return_times),
                'batch_serial_number': data.batch.batch_serial_number,
                'wave_serial_number': data.wave.wave_serial_number,
                'ean13': convert.EAN13Converter.convert_id_to_ean13(data.id),
                }
        return row

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

    def export_data(self, data: list[StorageCardDict]) -> None:
        """导出数据到Excel和数据库"""
        # 先获取最新的inventory_id
        latest_inventory_id = self._db_controller.get_latest_inventory_id()

        # 要先导出到数据库才能获取到id和EAN13
        data_list = []
        for each in data:
            data_list.append((each['name'], each['brand'], float(each['price']), each['batch_serial_number']))
        self._db_controller.export_to_database(data_list)

        new_data = self._db_controller.get_all_inventory_and_batch_greater_than_id(latest_inventory_id)
        # 将数据类对象转换为字典列表
        dict_list = [asdict(item) for item in new_data]

        # 创建一个DataFrame
        df = pd.DataFrame(dict_list)

        # 重新排序列以匹配所需的顺序
        df = df[['item_id', 'item_name', 'brand', 'price', 'batch_name', 'batch_serial_number', 'created_time']]

        # 对其中的item_id列全部调用函数转换成EAN13
        df['item_id'] = df['item_id'].apply(convert.EAN13Converter.convert_id_to_ean13)

        # 重命名列以匹配所需的标题
        df.columns = ['EAN13', '名称', '品牌', '价格', '批次名', '批次序号', '批次创建时间']

        # 将DataFrame导出为Excel文件
        save_dir = Path(cfg.get(cfg.storage_path))
        EXCEL_FILE = save_dir / f'入库信息{datetime.today().strftime("%Y-%m-%d-%H-%M-%S")}.xlsx'
        df.to_excel(EXCEL_FILE, index=False)
        loguru.logger.debug(f'导出数据到Excel文件:{EXCEL_FILE}')
        loguru.logger.debug(f'本次导出了{len(dict_list)}条数据到Excel文件')
        os.startfile(save_dir)

    def export_return_data(self, data: list[ReStorageDict]) -> None:
        """前往数据库中将他们的EAN13的return_times+1,同时将is_sold设置为0"""
        for each in data:
            self._db_controller.set_inventory_return_times_and_is_sold(each['ean13'])

    def is_real_ean13(self, ean13: str) -> bool:
        """检测是否是真实的EAN13"""
        return self._db_controller.is_real_ean13(ean13)

    def is_inventory_sold(self, ean13: str) -> bool:
        return self._db_controller.is_inventory_sold(ean13)


if __name__ == "__main__":
    s = StorageModel()
    print(s.get_inventory_by_ean13('0000000000017'))
