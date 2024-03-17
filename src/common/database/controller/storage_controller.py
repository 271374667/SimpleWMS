from dataclasses import dataclass
from datetime import datetime
from typing import List, Tuple

from src.common.database.entity import model
from src.common.database.query_filter import IdFilter
from src.common.database.service.add_model_service import AddModelService
from src.common.database.service.get_attribute_service import GetAttributeService
from src.common.database.service.get_model_service import GetModelService
from src.common.database.service.set_model_service import SetModelService
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
        self._set_model_service = SetModelService()

    def get_inventory_by_ean13(self, ean13: str) -> model.Inventory:
        """根据EAN13获取库存信息"""
        query = self._get_model_service.get_all_inventory()
        query = IdFilter.inventory_ean13(query, ean13)
        return query.first()

    def export_to_database(self, data: List[Tuple[str, str, float, str]]) -> None:
        """导出数据到数据库"""
        for item_name, brand, price, batch_serial_number in data:
            batch_name = convert.BatchConverter.convert_batch_serial_number_to_batch_name(batch_serial_number)
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
        query = self._get_model_service.get_all_inventory()
        query = IdFilter.inventory_id_greater_than(query, id)
        inventory_list = query.all()
        result = [
                StorageData(
                        item_id=inventory.id,
                        item_name=inventory.item_name,
                        brand=inventory.brand,
                        price=inventory.price,
                        batch_name=inventory.batch.batch_name,
                        batch_serial_number=inventory.batch.batch_serial_number,
                        created_time=inventory.batch.created_time,
                        )
                for inventory in inventory_list
                ]
        # 按照 id 字段排序
        result = sorted(result, key=lambda x: x.item_id)
        return result

    def get_latest_inventory_id(self) -> int:
        """获取最新的库存ID"""
        return self._get_attribute_service.get_inventory_latest_id()

    def is_real_ean13(self, ean13: str) -> bool:
        """检测是否是真实的EAN13"""
        really_ean13 = convert.EAN13Converter.convert_id_to_ean13(int(ean13[:12]))
        return really_ean13 == ean13

    def is_inventory_sold(self, ean13: str) -> bool:
        """检测库存是否已经出库"""
        query = self._get_model_service.get_all_inventory()
        query = IdFilter.inventory_ean13(query, ean13)
        result = query.first()
        return False if result is None else result.is_sold != 0

    def set_inventory_return_times_and_is_sold(self, ean13: str) -> None:
        """设置库存的退货次数和是否出库"""
        self._set_model_service.set_inventory_return_and_sold(ean13)

    def _is_batch_today(self, serial_number: str) -> bool:
        """判断这个批次是否是今天的"""
        today = datetime.now()

        query = self._get_model_service.get_all_batch()
        query = IdFilter.batch_serial_number(query, serial_number)
        batch_sqalchemy_model = query.first()
        if not batch_sqalchemy_model:
            return True
        batch_time = batch_sqalchemy_model.created_time
        return batch_time.year == today.year and batch_time.month == today.month and batch_time.day == today.day


if __name__ == '__main__':
    s = StorageController()
    a = ['202401001', '202401002', '202401001']
    # print(SType.get_latest_batch_serial_number())
