from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from src.common.database.entity.dataclass_model import Wave
from src.common.database.service.database_service import DatabaseService
from src.common.database.utils import convert


@dataclass
class RetrievalData:
    name: str
    brand: str
    price: float
    batch_name: str
    storage_time: datetime
    ean13: str


class RetrievalController:
    def __init__(self):
        self._db = DatabaseService()

    def get_inventory_by_ean13(self, ean13: str) -> Optional[RetrievalData]:
        result = self._db.get_inventory_by_ean13(ean13)
        if result is None:
            return None

        data = RetrievalData(name=result.item_name,
                             brand=result.brand,
                             price=result.price,
                             batch_name=result.batch.batch_name,
                             storage_time=result.batch.created_time,
                             ean13=ean13,
                             )
        return data

    def is_real_ean13(self, ean13: str) -> bool:
        """检测是否是真实的EAN13"""
        really_ean13 = convert.convert_id_to_ean13(int(ean13[:12]))
        if really_ean13 != ean13:
            return False
        return True

    def get_lastest_wave_serial_number(self) -> str:
        return self._db.get_lastst_wave_serial_number()

    def is_inventory_sold(self, ean13: str) -> bool:
        result = self._db.get_inventory_by_ean13(ean13)
        if result is None:
            return False
        return bool(result.is_sold)

    def set_inventory_sold(self, ean13: str, wave_serial_number: str) -> None:
        result = self._db.get_inventory_by_ean13(ean13)
        if result is None:
            return

        self._db.set_wave_for_inventory_by_dataclasses(ean13=ean13,
                                                       wave=Wave(wave_serial_number=wave_serial_number,
                                                                 wave_name=convert.convert_wave_serial_number_to_wave_name(
                                                                         wave_serial_number),
                                                                 created_time=datetime.now()))

    def convert_wave_serial_number_to_wave_name(self, wave_serial_number: str) -> str:
        return convert.convert_wave_serial_number_to_wave_name(wave_serial_number)
