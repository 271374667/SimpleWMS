from datetime import datetime

from typing_extensions import NotRequired, Required, TypedDict

from src.enums import BasicSearchCombboxOperationEnum


class CustomBaseDict(TypedDict):
    pass


class StorageDict(CustomBaseDict):
    name: Required[str]
    brand: Required[str]
    price: Required[float]
    batch_serial_number: Required[str]


class ReStorageDict(CustomBaseDict):
    name: Required[str]
    brand: Required[str]
    price: Required[float]
    storage_time: Required[datetime]
    return_times: Required[int]
    batch_serial_number: Required[str]
    wave_serial_number: Required[str]
    ean13: Required[str]


class RetrievalDict(CustomBaseDict):
    name: Required[str]
    brand: Required[str]
    price: Required[float]
    wave_serial_number: Required[str]
    storage_time: Required[datetime]
    ean13: Required[str]


class UnsalableDict(CustomBaseDict):
    name: Required[str]
    brand: Required[str]
    batch_serial_number: Required[str]
    storage_time_from_today: Required[int]
    storage_count: Required[int]
    total_count: Required[int]
    storage_rate: Required[float]


OutOfStockDict = UnsalableDict


class ReturnTimesDict(CustomBaseDict):
    name: Required[str]
    brand: Required[str]
    batch_serial_number: Required[str]
    storage_time: Required[datetime]
    return_times: Required[int]
    ean13: Required[str]


class BasicSearchDict(CustomBaseDict):
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
