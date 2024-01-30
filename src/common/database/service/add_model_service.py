from datetime import datetime

from src.common.database import Session
from src.common.database.entity import model
from src.common.database.service.get_model_service import GetModelService


class AddModelService:
    def __init__(self):
        self._session = Session()
        self._get_model_service = GetModelService()

    def add_inventory(self, item_name: str, price: float, brand: str, batch: model.Batch) -> model.Inventory:
        # 批次存在则获取批次，不存在则创建批次
        batch_sqlalchemy_model = self._get_model_service.get_batch_by_serial_number(batch.batch_serial_number)
        if batch_sqlalchemy_model is None:
            batch_sqlalchemy_model = batch

        inventory_sqlalchemy_model = model.Inventory(item_name=item_name,
                                                     price=price,
                                                     brand=brand,
                                                     batch=batch_sqlalchemy_model)
        self._session.add(inventory_sqlalchemy_model)
        self._session.commit()
        return inventory_sqlalchemy_model

    def add_batch(self, batch_serial_number: str, batch_name: str, created_time: datetime) -> model.Batch:
        batch_sqlalchemy_model = model.Batch(batch_serial_number=batch_serial_number,
                                             batch_name=batch_name,
                                             created_time=created_time)
        self._session.add(batch_sqlalchemy_model)
        self._session.commit()
        return batch_sqlalchemy_model

    def add_wave(self, wave_serial_number: str, wave_name: str, created_time: datetime) -> model.Wave:
        wave_sqlalchemy_model = model.Wave(wave_serial_number=wave_serial_number,
                                           wave_name=wave_name,
                                           created_time=created_time, )
        self._session.add(wave_sqlalchemy_model)
        self._session.commit()
        return wave_sqlalchemy_model
