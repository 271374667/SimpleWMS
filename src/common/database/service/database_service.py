from datetime import date, datetime
from typing import Optional, Union

import loguru
from sqlalchemy import and_

from src.common.database import Session
from src.common.database.entity import dataclass_model
from src.common.database.entity import model
from src.common.database.utils import convert, serial_number


class DatabaseService:
    def __init__(self):
        self._session = Session()

    def get_all_batch(self) -> list[model.Batch]:
        return self._session.query(model.Batch).all()

    def get_all_wave(self) -> list[model.Wave]:
        return self._session.query(model.Wave).all()

    def get_all_inventory(self) -> list[model.Inventory]:
        return self._session.query(model.Inventory).all()

    def get_all_batch_this_month(self) -> list[model.Batch]:
        """获取本月的所有批次"""
        today = date.today()
        return self._session.query(model.Batch).filter(model.Batch.created_time >= today.replace(day=1)).all()

    def get_all_inventory_this_month(self) -> list[model.Inventory]:
        """获取本月的所有商品"""
        today = date.today()
        return self._session.query(model.Inventory).filter(model.Inventory.batch.has(
                model.Batch.created_time >= today.replace(day=1))).all()

    def get_all_batch_serial_number_this_month(self) -> list[str]:
        batch_sqlalchemy_model = self.get_all_batch_this_month()
        return [x.batch_serial_number for x in batch_sqlalchemy_model]

    def get_all_wave_this_month(self) -> list[model.Wave]:
        """获取本月的所有波次"""
        today = date.today()
        return self._session.query(model.Wave).filter(model.Wave.created_time >= today.replace(day=1)).all()

    def get_all_wave_serial_number_this_month(self) -> list[str]:
        wave_sqlalchemy_model = self.get_all_wave_this_month()
        return [x.wave_serial_number for x in wave_sqlalchemy_model]

    def get_batch_by_serial_number(self, serial_number: str) -> Optional[model.Batch]:
        return self._session.query(model.Batch).filter(model.Batch.batch_serial_number == serial_number).first()

    def get_wave_by_serial_number(self, serial_number: str) -> Optional[model.Wave]:
        return self._session.query(model.Wave).filter(model.Wave.wave_serial_number == serial_number).first()

    def get_inventory_by_ean13(self, ean13: str) -> Optional[model.Inventory]:
        number = ean13[:12]
        return self._session.query(model.Inventory).filter(model.Inventory.id == int(number)).first()

    def get_inventory_greater_than_id(self, id: int) -> list[model.Inventory]:
        return self._session.query(model.Inventory).filter(model.Inventory.id > id).all()

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

    def get_latest_wave_serial_number(self) -> str:
        """获取最新的批次,如果不存在会自动生成一个"""
        today = date.today()
        batchs_this_month = self.get_all_wave_serial_number_this_month()
        if not batchs_this_month:
            loguru.logger.debug(f'本月没有任何波次，自动生成一个波次:{today.year}{today.month:02d}001')
            return f'{today.year}{today.month:02d}001'
        return serial_number.sort_serial_number(batchs_this_month)[0]

    def get_latest_batch_serial_number(self) -> str:
        """获取最新的批次,如果不存在会自动生成一个"""
        today = date.today()
        batchs_this_month = self.get_all_batch_serial_number_this_month()
        if not batchs_this_month:
            loguru.logger.debug(f'本月没有任何批次，自动生成一个批次:{today.year}{today.month:02d}001')
            return f'{today.year}{today.month:02d}001'
        return serial_number.sort_serial_number(batchs_this_month)[0]

    def get_unsold_inventory_this_month(self) -> list[model.Inventory]:
        """获取本月未售出的商品数量"""
        today = date.today()
        result = self._session.query(model.Inventory).filter(
                and_(model.Inventory.is_sold == 0,
                     model.Inventory.batch.has(model.Batch.created_time >= today.replace(day=1)))
                ).all()

        return result

    def get_unsold_inventory(self) -> list[model.Inventory]:
        """获取未售出的商品数量"""
        result = self._session.query(model.Inventory).filter(model.Inventory.is_sold == 0).all()
        return result


def add_wave(self, wave_serial_number: str, wave_name: str, created_time: datetime) -> model.Wave:
    wave_sqlalchemy_model = model.Wave(wave_serial_number=wave_serial_number,
                                       wave_name=wave_name,
                                       created_time=created_time, )
    self._session.add(wave_sqlalchemy_model)
    self._session.commit()
    return wave_sqlalchemy_model


def add_wave_by_dataclasses(self, wave: dataclass_model.Wave) -> model.Wave:
    wave_sqlalchemy_model = self.add_wave(wave_serial_number=wave.wave_serial_number,
                                          wave_name=wave.wave_name,
                                          created_time=wave.created_time, )
    return wave_sqlalchemy_model


def add_batch(self, batch_serial_number: str, batch_name: str, created_time: datetime) -> model.Batch:
    batch_sqlalchemy_model = model.Batch(batch_serial_number=batch_serial_number,
                                         batch_name=batch_name,
                                         created_time=created_time)
    self._session.add(batch_sqlalchemy_model)
    self._session.commit()
    return batch_sqlalchemy_model


def add_batch_by_dataclasses(self, batch: dataclass_model.Batch) -> model.Batch:
    batch_sqlalchemy_model = self.add_batch(batch_serial_number=batch.batch_serial_number,
                                            batch_name=batch.batch_name,
                                            created_time=batch.created_time)
    return batch_sqlalchemy_model


def add_inventory(self, item_name: str, price: float, brand: str, batch: dataclass_model.Batch) -> model.Inventory:
    # 批次存在则获取批次，不存在则创建批次
    batch_sqlalchemy_model = self.get_batch_by_serial_number(batch.batch_serial_number)
    if batch_sqlalchemy_model is None:
        batch_sqlalchemy_model = model.Batch(batch_serial_number=batch.batch_serial_number,
                                             batch_name=batch.batch_name,
                                             created_time=batch.created_time)

    inventory_sqlalchemy_model = model.Inventory(item_name=item_name,
                                                 price=price,
                                                 brand=brand,
                                                 batch=batch_sqlalchemy_model)
    self._session.add(inventory_sqlalchemy_model)
    self._session.commit()
    return inventory_sqlalchemy_model


def add_inventory_by_dataclasses(self, inventory: dataclass_model.Inventory) -> model.Inventory:
    inventory_sqlalchemy_model = self.add_inventory(item_name=inventory.item_name,
                                                    price=inventory.price,
                                                    brand=inventory.brand,
                                                    batch=inventory.batch)
    return inventory_sqlalchemy_model


def set_wave_for_inventory(self, ean13: Union[str, int], wave: model.Wave) -> None:
    # 获取 EAN13 对应的库存
    if isinstance(ean13, int):
        ean13 = convert.convert_id_to_ean13(ean13)
    elif isinstance(ean13, str) and len(ean13) == 12:
        ean13 = convert.convert_length12str_to_ean13(ean13)

    inventory_sqlalchemy_model = self.get_inventory_by_ean13(ean13)
    if not inventory_sqlalchemy_model:
        loguru.logger.warning(f"没有找到 EAN13 为 {ean13} 的商品")
        return

    # 先检查是否有这个波次，没有则创建,没有再使用传入的wave创建
    wave_sqlalchemy_model = self.get_wave_by_serial_number(wave.wave_serial_number)
    if wave_sqlalchemy_model is None:
        wave_sqlalchemy_model = wave

    inventory_sqlalchemy_model.wave = wave_sqlalchemy_model
    inventory_sqlalchemy_model.is_sold = 1
    self._session.commit()


def set_wave_for_inventory_by_dataclasses(self, ean13: Union[str, int],
                                          wave: dataclass_model.Wave) -> None:
    wave_sqlalchemy_model = model.Wave(wave_serial_number=wave.wave_serial_number,
                                       wave_name=wave.wave_name,
                                       created_time=wave.created_time)
    self.set_wave_for_inventory(ean13, wave_sqlalchemy_model)


def __del__(self):
    self._session.close()


if __name__ == "__main__":
    from pprint import pprint

    database_service = DatabaseService()
    # 创建一件商品并为他设置波次
    batch = dataclass_model.Batch(batch_serial_number="202301002", batch_name="test", created_time=datetime.today())
    inventory = dataclass_model.Inventory(item_name="Nike跑步鞋", price=331.0, brand="Nike", batch=batch)
    wave = dataclass_model.Wave(wave_serial_number="202301003", wave_name="第三波", created_time=datetime.today())

    database_service.add_inventory_by_dataclasses(inventory)
    database_service.set_wave_for_inventory_by_dataclasses(2, wave)

    pprint(database_service.get_all_batch())
    pprint(database_service.get_all_wave())
    pprint(database_service.get_all_inventory())
