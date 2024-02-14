from typing_extensions import Required, TypedDict


class CustomBaseDict(TypedDict):
    pass


class StorageDict(CustomBaseDict):
    name: Required[str]
    brand: Required[str]
    price: Required[str]
    batch_serial_number: Required[str]


class RetrievalDict(CustomBaseDict):
    name: Required[str]
    brand: Required[str]
    price: Required[str]
    wave_serial_number: Required[str]
    storage_time: Required[str]
    ean13: Required[str]


class UnsalableDict(CustomBaseDict):
    name: Required[str]
    brand: Required[str]
    batch_serial_number: Required[str]
    storage_time_from_today: Required[str]
    storage_count: Required[str]
    total_count: Required[str]
    storage_rate: Required[str]
