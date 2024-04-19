"""WMS 数据类,负责存储 WMS 模块的数据类.

因为需要在表格里面显示表头,所以字段都是中文
"""

from abc import ABC
from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from PySide6.QtCore import Qt
from sqlalchemy.sql import sqltypes

from src.core.enums import BasicSearchCombboxOperationEnum


class DataclassBase(ABC):
    pass


@dataclass(slots=True, frozen=True)
class BasicSearchDataclass(DataclassBase):
    """基本查询"""

    Ean13码: str
    商品名称: str
    品牌名称: str
    价格: float
    批次编号: str
    入库时间: datetime
    入库天数: int
    退货次数: int
    是否售出: bool
    波次编号: Optional[str] = "无波次"
    出库时间: Optional[datetime] = None


@dataclass(slots=True, frozen=True)
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
    sort_by: Optional[str] = None
    sort_order: Optional[Qt.SortOrder] = None
    has_sort: Optional[bool] = None


@dataclass(slots=True, frozen=True)
class UnsalableDataclass(DataclassBase):
    """滞销"""

    商品名称: str
    品牌名称: str
    批次编号: str
    入库天数: int
    库存量: int
    总数: int
    存货率: float


@dataclass(slots=True, frozen=True)
class OutOfStockDataclass(DataclassBase):
    """脱销"""

    商品名称: str
    品牌名称: str
    批次编号: str
    入库天数: int
    库存量: int
    总数: int
    存货率: float


@dataclass(slots=True, frozen=True)
class ReturnTimesDataclass(DataclassBase):
    """退货次数"""

    商品名称: str
    品牌名称: str
    批次编号: str
    入库时间: datetime
    退货次数: int
    Ean13码: str
