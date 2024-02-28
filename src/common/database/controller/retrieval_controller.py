from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from src.common.database.entity import model
from src.common.database.service.get_attribute_service import GetAttributeService
from src.common.database.service.get_model_service import GetModelService
from src.common.database.service.set_model_service import SetModelService
from src.common.database.utils import convert
from src.common.database.query_filter import IdFilter


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
        self._set_model_service = SetModelService()
        self._get_attribute_service = GetAttributeService()
        self._get_model_service = GetModelService()

    def get_inventory_by_ean13(self, ean13: str) -> Optional[RetrievalData]:
        query = self._get_model_service.get_all_inventory()
        query = IdFilter.inventory_ean13(query, ean13)
        result = query.first()
        if result is None:
            return None

        return RetrievalData(
                name=result.item_name,
                brand=result.brand,
                price=result.price,
                batch_name=result.batch.batch_name,
                storage_time=result.batch.created_time,
                ean13=ean13,
                )

    def is_real_ean13(self, ean13: str) -> bool:
        """检测是否是真实的EAN13"""
        really_ean13 = convert.EAN13Converter.convert_id_to_ean13(int(ean13[:12]))
        return really_ean13 == ean13

    def get_lastest_wave_serial_number(self) -> str:
        return self._get_attribute_service.get_latest_wave_serial_number()

    def is_inventory_sold(self, ean13: str) -> bool:
        query = self._get_model_service.get_all_inventory()
        query = IdFilter.inventory_ean13(query, ean13)
        result = query.first()
        return False if result is None else bool(result.is_sold)

    def set_inventory_sold(self, ean13: str, wave_serial_number: str) -> None:
        query = self._get_model_service.get_all_inventory()
        query = IdFilter.inventory_ean13(query, ean13)
        result = query.first()
        if result is None:
            return

        self._set_model_service.set_wave_for_inventory(ean13=ean13,
                                                       wave=model.Wave(wave_serial_number=wave_serial_number,
                                                                       wave_name=convert.WaveConverter.convert_wave_serial_number_to_wave_name(
                                                                               wave_serial_number)
                                                                       )
                                                       )

    def convert_wave_serial_number_to_wave_name(self, wave_serial_number: str) -> str:
        return convert.WaveConverter.convert_wave_serial_number_to_wave_name(wave_serial_number)
