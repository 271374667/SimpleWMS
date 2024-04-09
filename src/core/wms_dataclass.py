from abc import ABC
from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from src.core.enums import BasicSearchCombboxOperationEnum


class DataclassBase(ABC):
    pass


@dataclass
class BasicSearchDataclass(DataclassBase):
    """基本查询"""

    ean13: str
    name: str
    brand: str
    price: float
    batch_serial_number: str
    storage_time: datetime
    storage_time_from_today: int
    return_times: int
    wave_serial_number: Optional[str] = "无波次"
    retrieval_time: Optional[datetime] = None
    is_sold: Optional[bool] = None  # 将 int 转换成 "是" 或者 "否"


@dataclass
class BasicSearchParameterDataclass(DataclassBase):
    """基本查询参数"""

    ean13: Optional[str] = None
    name: Optional[str] = None
    brand: Optional[str] = None
    has_price: Optional[bool] = None
    price: Optional[float] = None
    price_operation: Optional[BasicSearchCombboxOperationEnum] = None
    batch_serial_number: Optional[str] = None
    wave_serial_number: Optional[str] = None
    has_storage_days: Optional[bool] = None
    storage_days: Optional[int] = None
    storage_days_operation: Optional[BasicSearchCombboxOperationEnum] = None
    hide_sold_item: Optional[bool] = None
    hide_has_return_item: Optional[bool] = None
