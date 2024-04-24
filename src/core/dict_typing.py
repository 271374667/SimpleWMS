from datetime import datetime

from typing_extensions import NotRequired, Required, TypedDict


class CustomBaseDict(TypedDict):
    pass


class StorageDict(CustomBaseDict):
    """入库"""

    name: Required[str]
    brand: Required[str]
    price: Required[float]
    batch_serial_number: Required[str]


class ReStorageDict(CustomBaseDict):
    """退货重新入库"""

    name: Required[str]
    brand: Required[str]
    price: Required[float]
    storage_time: Required[datetime]
    return_times: Required[int]
    batch_serial_number: Required[str]
    wave_serial_number: Required[str]
    ean13: Required[str]


class RetrievalDict(CustomBaseDict):
    """出库"""

    name: Required[str]
    brand: Required[str]
    price: Required[float]
    wave_serial_number: Required[str]
    storage_time: Required[datetime]
    ean13: Required[str]


class AllInventoryDict(CustomBaseDict):
    """所有的数据,用于导出和导入"""

    ean13: Required[str]
    name: Required[str]
    brand: Required[str]
    price: Required[float]
    is_sold: Required[int]
    return_times: Required[int]
    is_inventory_active: Required[int]
    batch_id: Required[int]
    batch_name: Required[str]
    batch_serial_number: Required[str]
    batch_created_time: Required[datetime]
    is_batch_active: Required[int]
    wave_id: NotRequired[int]
    wave_name: NotRequired[str]
    wave_serial_number: NotRequired[str]
    wave_created_time: NotRequired[datetime]
    is_wave_active: NotRequired[int]


# 下面是 home 页面里面 card 表格的字典
class BatchCardDict(CustomBaseDict):
    batch_serial_number: Required[str]
    batch_created_time: Required[datetime]
    item_quantity: Required[int]


class WaveCardDict(CustomBaseDict):
    wave_serial_number: Required[str]
    wave_created_time: Required[datetime]
    item_quantity: Required[int]


class ItemQuantityCardDict(CustomBaseDict):
    name: Required[str]
    brand: Required[str]
    item_quantity: Required[int]


class MoneyCardDict(CustomBaseDict):
    name: Required[str]
    brand: Required[str]
    price: Required[float]


class StorageCardDict(CustomBaseDict):
    name: Required[str]
    brand: Required[str]
    storage_number: Required[float]


class RetrievalCardDict(CustomBaseDict):
    name: Required[str]
    brand: Required[str]
    retrieval_number: Required[float]
