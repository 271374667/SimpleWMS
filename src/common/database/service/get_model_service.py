from datetime import date
from typing import Optional

from sqlalchemy import and_, func

from src.common.database import Session
from src.common.database.entity import model


# TODO: 之后所有的查询都会使用 select() 方法进行重写,然后再 controller 中再进行调用以此来提高性能
class GetModelService:
    def __init__(self):
        self._session = Session

    # 基础查询
    def get_all_inventory(self) -> list[model.Inventory]:
        return self._session.query(model.Inventory).all()

    def get_all_batch(self) -> list[model.Batch]:
        return self._session.query(model.Batch).all()

    def get_all_wave(self) -> list[model.Wave]:
        return self._session.query(model.Wave).all()

    # 通过属性查询
    def get_inventory_greater_than_id(self, id: int) -> list[model.Inventory]:
        return self._session.query(model.Inventory).filter(model.Inventory.id > id).all()

    def get_inventory_by_ean13(self, ean13: str) -> Optional[model.Inventory]:
        number = ean13[:12]
        return self._session.query(model.Inventory).filter(model.Inventory.id == int(number)).first()

    def get_wave_by_serial_number(self, serial_number: str) -> Optional[model.Wave]:
        return self._session.query(model.Wave).filter(model.Wave.wave_serial_number == serial_number).first()

    def get_batch_by_serial_number(self, serial_number: str) -> Optional[model.Batch]:
        return self._session.query(model.Batch).filter(model.Batch.batch_serial_number == serial_number).first()

    # 按照时间进行获取
    # TODO: 这里的时间都必须要高度抽象，之后要改成两个时间参数获取值,比如start_datetime, end_datetime
    def get_all_inventory_this_month(self) -> list[model.Inventory]:
        """获取本月的所有商品"""
        today = date.today()
        return self._session.query(model.Inventory).filter(model.Inventory.batch.has(
                model.Batch.created_time >= today.replace(day=1))).all()

    def get_all_batch_this_month(self) -> list[model.Batch]:
        """获取本月的所有批次"""
        today = date.today()
        return self._session.query(model.Batch).filter(model.Batch.created_time >= today.replace(day=1)).all()

    def get_all_wave_this_month(self) -> list[model.Wave]:
        """获取本月的所有波次"""
        today = date.today()
        return self._session.query(model.Wave).filter(model.Wave.created_time >= today.replace(day=1)).all()

    # 按照是否售出进行获取
    def get_unsold_inventory(self) -> list[model.Inventory]:
        """获取未售出的商品数量"""
        result = self._session.query(model.Inventory).filter(model.Inventory.is_sold == 0).all()
        return result

    def get_unsold_inventory_this_month(self) -> list[model.Inventory]:
        """获取本月未售出的商品数量"""
        today = date.today()
        result = self._session.query(model.Inventory).filter(
                and_(model.Inventory.is_sold == 0,
                     model.Inventory.batch.has(model.Batch.created_time >= today.replace(day=1)))
                ).all()

        return result

