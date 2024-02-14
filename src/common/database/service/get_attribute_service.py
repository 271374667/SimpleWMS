from datetime import date
from datetime import datetime

import loguru
from sqlalchemy import func

from src.common.database import Session
from src.common.database.entity import model
from src.common.database.service.get_model_service import GetModelService
from src.common.database.utils import serial_number


class GetAttributeService:
    def __init__(self):
        self._session = Session
        self._get_model_service = GetModelService()

    # 返回 id
    def get_batch_latest_id(self) -> int:
        batch = self._session.query(model.Batch).order_by(model.Batch.id.desc()).first()
        if batch is None:
            return 0
        return batch.id

    def get_wave_latest_id(self) -> int:
        wave = self._session.query(model.Wave).order_by(model.Wave.id.desc()).first()
        if wave is None:
            return 0
        return wave.id

    def get_inventory_latest_id(self) -> int:
        inventory = self._session.query(model.Inventory).order_by(model.Inventory.id.desc()).first()
        if inventory is None:
            return 0
        return inventory.id

    # 返回 serial_number
    def get_all_batch_serial_number_this_month(self) -> list[str]:
        batch_sqlalchemy_model = self._get_model_service.get_all_batch_this_month()
        return [x.batch_serial_number for x in batch_sqlalchemy_model]

    def get_all_wave_serial_number_this_month(self) -> list[str]:
        wave_sqlalchemy_model = self._get_model_service.get_all_wave_this_month()
        return [x.wave_serial_number for x in wave_sqlalchemy_model]

    def get_latest_batch_serial_number(self) -> str:
        """获取最新的批次,如果不存在会自动生成一个"""
        today = date.today()
        batchs_this_month = self.get_all_batch_serial_number_this_month()
        if not batchs_this_month:
            loguru.logger.debug(f'本月没有任何批次，自动生成一个批次:{today.year}{today.month:02d}001')
            return f'{today.year}{today.month:02d}001'
        return serial_number.sort_serial_number(batchs_this_month)[0]

    def get_latest_wave_serial_number(self) -> str:
        """获取最新的批次,如果不存在会自动生成一个"""
        today = date.today()
        batchs_this_month = self.get_all_wave_serial_number_this_month()
        if not batchs_this_month:
            loguru.logger.debug(f'本月没有任何波次，自动生成一个波次:{today.year}{today.month:02d}001')
            return f'{today.year}{today.month:02d}001'
        return serial_number.sort_serial_number(batchs_this_month)[0]

    # 分组获取
    def get_sold_inventory_and_count_group_by_batch_brand_name(self) -> list[tuple[str, str, str, datetime, int]]:
        """获取已售出的商品数量"""
        result = (self._session.query(model.Inventory.item_name,
                                      model.Inventory.brand,
                                      model.Batch.batch_serial_number,
                                      model.Batch.created_time,
                                      func.count(1))
                  .join(model.Batch,
                        model.Inventory.batch_id == model.Batch.id)
                  .filter(
                model.Inventory.is_sold == 1)
                  .group_by(model.Inventory.batch_id,
                            model.Inventory.brand,
                            model.Inventory.item_name).all()
                  )
        return result

    def get_unsold_inventory_and_count_group_by_batch_brand_name(self) -> list[tuple[str, str, str, datetime, int]]:
        """获取未售出的商品数量"""
        result = (self._session.query(model.Inventory.item_name,
                                      model.Inventory.brand,
                                      model.Batch.batch_serial_number,
                                      model.Batch.created_time,
                                      func.count(1))
                  .join(model.Batch,
                        model.Inventory.batch_id == model.Batch.id)
                  .filter(
                model.Inventory.is_sold == 0)
                  .group_by(model.Inventory.batch_id,
                            model.Inventory.brand,
                            model.Inventory.item_name).all()
                  )
        return result

    def get_all_inventory_and_count_group_by_batch_brand_name(self) -> list[tuple[str, str, str, datetime, int]]:
        """获取所有的商品数量"""
        result = (self._session.query(model.Inventory.item_name,
                                      model.Inventory.brand,
                                      model.Batch.batch_serial_number,
                                      model.Batch.created_time,
                                      func.count(1))
                  .join(model.Batch,
                        model.Inventory.batch_id == model.Batch.id)
                  .group_by(model.Inventory.batch_id,
                            model.Inventory.brand,
                            model.Inventory.item_name).all()
                  )
        return result


if __name__ == '__main__':
    from pprint import pprint

    g = GetAttributeService()
    # print(g.get_latest_batch_serial_number())
    pprint(g.get_all_inventory_and_count_group_by_batch_brand_name())
