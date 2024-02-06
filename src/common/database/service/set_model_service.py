from typing import Union

import loguru

from src.common.database import Session
from src.common.database.entity import model
from src.common.database.service.get_model_service import GetModelService
from src.common.database.utils import convert


class SetModelService:
    def __init__(self):
        self._session = Session
        self._get_model_service = GetModelService()

    def set_wave_for_inventory(self, ean13: Union[str, int], wave: model.Wave) -> None:
        # 获取 EAN13 对应的库存
        if isinstance(ean13, int):
            ean13 = convert.EAN13Converter.convert_id_to_ean13(ean13)
        elif isinstance(ean13, str) and len(ean13) == 12:
            ean13 = convert.EAN13Converter.convert_length12str_to_ean13(ean13)

        inventory_sqlalchemy_model = self._get_model_service.get_inventory_by_ean13(ean13)
        if not inventory_sqlalchemy_model:
            loguru.logger.warning(f"没有找到 EAN13 为 {ean13} 的商品")
            return

        # 先检查是否有这个波次，没有则创建,没有再使用传入的wave创建
        wave_sqlalchemy_model = self._get_model_service.get_wave_by_serial_number(wave.wave_serial_number)
        if wave_sqlalchemy_model is None:
            self._session.add(wave)
            wave_sqlalchemy_model = wave

        inventory_sqlalchemy_model.wave = wave_sqlalchemy_model
        inventory_sqlalchemy_model.is_sold = 1
        self._session.commit()
