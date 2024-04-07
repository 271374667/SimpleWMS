from datetime import datetime

from typing_extensions import NotRequired, Required, TypedDict

from src.core.enums import BasicSearchCombboxOperationEnum


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


class UnsalableDict(CustomBaseDict):
    """滞销"""

    name: Required[str]
    brand: Required[str]
    batch_serial_number: Required[str]
    storage_time_from_today: Required[int]
    storage_count: Required[int]
    total_count: Required[int]
    storage_rate: Required[float]


# 脱销
OutOfStockDict = UnsalableDict


class ReturnTimesDict(CustomBaseDict):
    """退货次数"""

    name: Required[str]
    brand: Required[str]
    batch_serial_number: Required[str]
    storage_time: Required[datetime]
    return_times: Required[int]
    ean13: Required[str]


class BasicSearchDict(CustomBaseDict):
    """基本查询"""

    name: Required[str]
    brand: Required[str]
    price: Required[float]
    batch_serial_number: Required[str]
    storage_time: Required[datetime]
    storage_time_from_today: Required[int]
    return_times: Required[int]
    wave_serial_number: NotRequired[str]
    retrieval_time: NotRequired[datetime]
    is_sold: NotRequired[str]  # 将 int 转换成 "是" 或者 "否"
    ean13: Required[str]


class BasicSearchParameterDict(CustomBaseDict):
    """基本查询参数"""

    ean13: NotRequired[str]
    name: NotRequired[str]
    brand: NotRequired[str]
    has_price: NotRequired[bool]
    price: NotRequired[float]
    price_operation: NotRequired[BasicSearchCombboxOperationEnum]
    batch_serial_number: NotRequired[str]
    wave_serial_number: NotRequired[str]
    has_storage_days: NotRequired[bool]
    storage_days: NotRequired[int]
    storage_days_operation: NotRequired[BasicSearchCombboxOperationEnum]
    hide_sold_item: NotRequired[bool]
    hide_has_return_item: NotRequired[bool]


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
