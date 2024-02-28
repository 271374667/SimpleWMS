from typing import Optional
from typing import Union

import loguru

from src.common.database import Session
from src.common.database.entity import model
from src.common.database.query_filter import IdFilter
from src.common.database.service.get_model_service import GetModelService
from src.common.database.utils import convert

class SetModelService:
    def __init__(self):
        self._session = Session
        self._get_model_service = GetModelService()

    def set_wave_for_inventory(self, ean13: Union[str, int], wave: Optional[model.Wave]) -> None:
        """设置波次
        Args:
            ean13: 物品的EAN13编码
            wave: 波次信息,如果为None则表示是设置退货
        """
        # 获取 EAN13 对应的库存
        if isinstance(ean13, int):
            ean13 = convert.EAN13Converter.convert_id_to_ean13(ean13)
        elif isinstance(ean13, str) and len(ean13) == 12:
            ean13 = convert.EAN13Converter.convert_length12str_to_ean13(ean13)

        # 检查是否有这个物品
        query = self._get_model_service.get_all_inventory()
        query = IdFilter.inventory_ean13(query, ean13)
        inventory_sqlalchemy_model = query.first()
        if not inventory_sqlalchemy_model:
            loguru.logger.warning(f"没有找到 EAN13 为 {ean13} 的商品")
            return

        # 如果为wave为None则表示是设置退货
        if wave is None:
            inventory_sqlalchemy_model.is_sold = 0
            inventory_sqlalchemy_model.return_times += 1
            inventory_sqlalchemy_model.wave = None
            inventory_sqlalchemy_model.wave_id = None
            loguru.logger.debug(f"设置 EAN13 为 {ean13} 的商品为退货")
            return

        # 检查是否有这个波次,没有则创建,没有再使用传入的wave创建
        query = self._get_model_service.get_all_wave()
        query = IdFilter.wave_serial_number(query, wave.wave_serial_number)
        wave_sqlalchemy_model = query.first()
        if wave_sqlalchemy_model is None:
            self._session.add(wave)
            wave_sqlalchemy_model = wave

        inventory_sqlalchemy_model.wave = wave_sqlalchemy_model
        inventory_sqlalchemy_model.is_sold = 1
        self._session.commit()
        loguru.logger.debug(f"设置 EAN13 为 {ean13} 的商品为波次 {wave.wave_serial_number}")

    def set_inventory_return_and_sold(self, ean13: str) -> None:
        """设置库存为退货和已售出,同时清空他的波次信息"""
        query = self._get_model_service.get_all_inventory()
        query = IdFilter.inventory_ean13(query, ean13)
        inventory_sqlalchemy_model = query.first()
        if not inventory_sqlalchemy_model:
            loguru.logger.warning(f"没有找到 EAN13 为 {ean13} 的商品")
            return

        inventory_sqlalchemy_model.is_sold = 0
        inventory_sqlalchemy_model.return_times += 1
        inventory_sqlalchemy_model.wave = None
        inventory_sqlalchemy_model.wave_id = None
        self._session.commit()
        loguru.logger.debug(f"设置 EAN13 为 {ean13} 的商品为退货")
