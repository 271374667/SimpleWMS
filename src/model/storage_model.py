from dataclasses import asdict
from datetime import datetime
from typing import Sequence, Tuple

import pandas as pd

from src.common.database.controller.storage_controller import StorageController
from src.common.database.utils import convert
from src.constant import EXCEL_FILE


class StorageModel:
    def __init__(self):
        self._db = StorageController()

    def get_newest_batch_serial_number(self) -> str:
        """获取最新的批次"""
        return self._db.get_latest_batch_serial_number()

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

    def export_data(self, data: Sequence[Tuple[str, str, float, int]]) -> None:
        """导出数据到Excel和数据库"""

        # 要先导出到数据库才能获取到id和EAN13
        # self._db.export_to_database(data)

        # 先获取最新的inventory_id
        latest_inventory_id = self._db.get_latest_inventory_id()
        new_data = self._db.get_all_inventory_and_batch_greater_than_id(latest_inventory_id)

        # 将数据类对象转换为字典列表
        dict_list = [asdict(item) for item in new_data]

        # 创建一个DataFrame
        df = pd.DataFrame(dict_list)
        df.dropna(axis=0, how='any', inplace=True)

        # 重新排序列以匹配所需的顺序
        df = df[['item_id', 'item_name', 'brand', 'price', 'batch_name', 'batch_serial_number', 'created_time']]

        # 对其中的item_id列全部调用函数转换成EAN13
        df['item_id'] = df['item_id'].apply(convert.convert_id_to_ean13)

        # 重命名列以匹配所需的标题
        df.columns = ['EAN13', '商品名称', '品牌', '价格', '批次名', '批次序号', '批次创建时间']

        # 将DataFrame导出为Excel文件
        df.to_excel(EXCEL_FILE, index=False)


if __name__ == "__main__":
    s = StorageModel()
