from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


@dataclass
class Batch:
    batch_serial_number: str
    batch_name: str
    created_time: datetime = field(default_factory=datetime.today)


@dataclass
class Wave:
    wave_serial_number: str
    wave_name: str
    created_time: datetime = field(default_factory=datetime.today)


@dataclass
class Inventory:
    item_name: str
    price: float
    brand: str
    batch: Batch
    wave: Optional[Wave] = field(default=None)
    is_sold: Optional[int] = 0
