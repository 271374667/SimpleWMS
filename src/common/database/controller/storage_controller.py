from dataclasses import dataclass
from datetime import datetime
from typing import List, Tuple

from src.common.database.entity import model
from src.common.database.service.add_model_service import AddModelService
from src.common.database.service.get_attribute_service import GetAttributeService
from src.common.database.service.get_model_service import GetModelService
from src.common.database.utils import convert


@dataclass(order=True)
class StorageData:
    item_id: int
    item_name: str
    brand: str
    price: float
    batch_name: str
    batch_serial_number: str
    created_time: datetime


class StorageController:
    def __init__(self):
        self._add_model_service = AddModelService()
        self._get_attribute_service = GetAttributeService()
        self._get_model_service = GetModelService()

    def export_to_database(self, data: List[Tuple[str, str, float, str]]) -> None:
        """导出数据到数据库"""
        for item_name, brand, price, batch_serial_number in data:
            batch_name = convert.convert_batch_serial_number_to_batch_name(batch_serial_number)
            batch_sqlalchemy_model = model.Batch(batch_serial_number=batch_serial_number,
                                                 batch_name=batch_name)
            self._add_model_service.add_inventory(item_name=item_name,
                                                  price=price,
                                                  brand=brand,
                                                  batch=batch_sqlalchemy_model)

    def get_latest_batch_serial_number(self) -> str:
        """获取最新的批次,如果不存在会自动生成一个"""
        return self._get_attribute_service.get_latest_batch_serial_number()

    def get_all_inventory_and_batch_greater_than_id(self, id: int) -> List[StorageData]:
        """获取所有的库存信息

        返回值不仅仅是库存信息，还包括了批次信息
        返回的数据格式为一个InventoryAndBatchInfo内容如下：
            [名称，品牌，价格，批次名称，批次序号，批次创建时间]
        """
        inventory_list = self._get_model_service.get_inventory_greater_than_id(id)
        result = []
        for inventory in inventory_list:
            result.append(StorageData(item_id=inventory.id,
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
        return self._get_attribute_service.get_inventory_latest_id()


if __name__ == '__main__':
    s = StorageController()
    a = ['202401001', '202401002', '202401001']
    # print(s.get_latest_batch_serial_number())
