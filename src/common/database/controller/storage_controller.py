from dataclasses import dataclass
from datetime import datetime
from typing import List, Tuple

from src.common.database.entity.dataclass_model import Batch, Inventory
from src.common.database.service.database_service import DatabaseService


@dataclass(order=True)
class InventoryAndBatchInfo:
    item_id: int
    item_name: str
    brand: str
    price: float
    batch_name: str
    batch_serial_number: str
    created_time: datetime


class StorageController:
    def __init__(self):
        self._db = DatabaseService()

    def export_to_database(self, data: List[Tuple[str, str, str, str]]) -> None:
        """导出数据到数据库"""
        for item_name, brand, price, batch in data:
            batch = Batch(batch_serial_number=batch, batch_name=batch)
            inventory = Inventory(item_name=item_name, price=price, brand=brand, batch=batch)
            self._db.add_inventory_by_dataclasses(inventory)

    def get_latest_batch_serial_number(self) -> str:
        """获取最新的批次,如果不存在会自动生成一个"""
        today = datetime.today()
        batchs_this_month = self._db.get_all_batch_serial_number_this_month()
        if not batchs_this_month:
            return f'{today.year}{datetime.month:02d}001'
        return batchs_this_month[0]

    def _sort_serial_number(self, serial_number_list: list[str]) -> list[str]:
        # 使用内置的sorted函数进行排序，key参数用于指定排序的依据
        # 这里我们先按照年份和月份排序，然后再按照序号排序
        # 因为我们希望年份和月份最新的以及序号大的排在前面，所以使用了负数
        sorted_list = sorted(serial_number_list, key=lambda x: (-int(x[:6]), -int(x[6:])))
        return sorted_list

    def get_all_inventory_and_batch_greater_than_id(self, id: int) -> List[InventoryAndBatchInfo]:
        """获取所有的库存信息

        返回值不仅仅是库存信息，还包括了批次信息
        返回的数据格式为一个InventoryAndBatchInfo内容如下：
            [名称，品牌，价格，批次名称，批次序号，批次创建时间]
        """
        inventory_list = self._db.get_inventory_greater_than_id(id)
        result = []
        for inventory in inventory_list:
            result.append(InventoryAndBatchInfo(item_id=inventory.id,
                                                item_name=inventory.item_name,
                                                brand=inventory.brand,
                                                price=inventory.price,
                                                batch_name=inventory.batch.batch_name,
                                                batch_serial_number=inventory.batch.batch_serial_number,
                                                created_time=inventory.batch.created_time))
        # 按照 id 字段排序
        result = sorted(result, key=lambda x: x.item_id)
        return result

    def get_latest_inventory_id(self) -> int:
        """获取最新的库存ID"""
        return self._db.get_batch_latest_id()


if __name__ == '__main__':
    s = StorageController()
    # a = ['197601003', '202301001', '202301002']
    # print(s._sort_serial_number(a))
    print(s.get_latest_batch_serial_number())
    print(s.get_all_inventory_and_batch())
