from datetime import datetime

from typing_extensions import Required, TypedDict


class CustomBaseDict(TypedDict):
    pass


class StorageDict(CustomBaseDict):
    name: Required[str]
    brand: Required[str]
    price: Required[float]
    batch_serial_number: Required[str]


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
