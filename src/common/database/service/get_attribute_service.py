from datetime import date
from datetime import datetime
from typing import Tuple

import loguru
from sqlalchemy import func

from src.common.database import Session
from src.common.database.entity import model
from src.common.database.query_filter import TimeFilter, TimeFilterEnum
from src.common.database.service.get_model_service import GetModelService
from src.common.database.utils import serial_number


class GetAttributeService:
    def __init__(self):
        self._session = Session
        self._get_model_service = GetModelService()

    # 返回 id
    def get_batch_latest_id(self) -> int:
        batch = self._session.query(model.Batch).order_by(model.Batch.id.desc()).first()
        return 0 if batch is None else batch.id

    def get_wave_latest_id(self) -> int:
        wave = self._session.query(model.Wave).order_by(model.Wave.id.desc()).first()
        return 0 if wave is None else wave.id

    def get_inventory_latest_id(self) -> int:
        inventory = (
            self._session.query(model.Inventory)
            .order_by(model.Inventory.id.desc())
            .first()
        )
        return 0 if inventory is None else inventory.id

    # 返回 serial_number
    def get_all_batch_serial_number_this_month(self) -> list[str]:
        query = self._get_model_service.get_all_batch()
        query = TimeFilter.batch_created_time(
            query, time_filter_enum=TimeFilterEnum.Month
        )
        batch_sqlalchemy_model = query.all()
        return [x.batch_serial_number for x in batch_sqlalchemy_model]

    def get_all_wave_serial_number_this_month(self) -> list[str]:
        query = self._get_model_service.get_all_wave()
        query = TimeFilter.wave_created_time(
            query, time_filter_enum=TimeFilterEnum.Month
        )
        wave_sqlalchemy_model = query.all()
        return [x.wave_serial_number for x in wave_sqlalchemy_model]

    def get_latest_batch_serial_number(self) -> str:
        """获取最新的批次,如果不存在会自动生成一个"""
        today = date.today()
        year = today.year
        month = today.month

        # 如果本月没有任何批次,那么就自动生成一个
        batchs_this_month = self.get_all_batch_serial_number_this_month()
        if not batchs_this_month:
            loguru.logger.debug(
                f"本月没有任何批次,自动生成一个批次号{year}{month:02d}001"
            )
            return f"{year}{month:02d}001"

        latest_batch_query = self._get_model_service.get_all_batch().order_by(
            model.Batch.id.desc()
        )
        latest_batch = latest_batch_query.first()
        # 如果最新批次存在而且是今天的批次,那么就返回最新批次
        if latest_batch.created_time.day == today.day:
            loguru.logger.debug(
                f"今天已经有一个批次了,批次号为{latest_batch.batch_serial_number}"
            )
            return latest_batch.batch_serial_number

        # 如果最新批次不是今天的批次,那么就在最新批次的基础上+1
        latest_batch_serial_number = latest_batch.batch_serial_number
        lastest_batch_int = serial_number.parser_serial_number_to_int(
            latest_batch_serial_number
        )
        return f"{year}{month:02d}{lastest_batch_int + 1:03d}"

    def get_latest_wave_serial_number(self) -> str:
        """获取最新的批次,如果不存在会自动生成一个"""
        today = date.today()
        year = today.year
        month = today.month

        # 如果本月没有任何批次,那么就自动生成一个
        waves_this_month = self.get_all_wave_serial_number_this_month()
        if not waves_this_month:
            loguru.logger.debug(
                f"本月没有任何批次,自动生成一个批次号{year}{month:02d}001"
            )
            return f"{year}{month:02d}001"

        latest_wave_query = self._get_model_service.get_all_wave().order_by(
            model.Wave.id.desc()
        )
        latest_wave = latest_wave_query.first()
        # 如果最新批次存在而且是今天的批次,那么就返回最新批次
        if latest_wave.created_time.day == today.day:
            loguru.logger.debug(
                f"今天已经有一个批次了,批次号为{latest_wave.wave_serial_number}"
            )
            return latest_wave.wave_serial_number

        # 如果最新批次不是今天的批次,那么就在最新批次的基础上+1
        latest_wave_serial_number = latest_wave.wave_serial_number
        lastest_wave_int = serial_number.parser_serial_number_to_int(
            latest_wave_serial_number
        )
        return f"{year}{month:02d}{lastest_wave_int + 1:03d}"

    # 分组获取
    def get_sold_inventory_and_count_group_by_batch_brand_name(
        self,
    ) -> list[tuple[str, str, str, datetime, int, int]]:
        """获取已售出的商品数量"""
        return (
            self._session.query(
                model.Inventory.item_name,
                model.Inventory.brand,
                model.Batch.batch_serial_number,
                model.Batch.created_time,
                func.count(1),
                model.Inventory.return_times,
            )
            .join(model.Batch, model.Inventory.batch_id == model.Batch.id)
            .filter(model.Inventory.is_sold == 1)
            .group_by(
                model.Inventory.batch_id,
                model.Inventory.brand,
                model.Inventory.item_name,
            )
            .all()
        )

    def get_unsold_inventory_and_count_group_by_batch_brand_name(
        self,
    ) -> list[Tuple[str, str, str, datetime, int, int]]:
        """获取未售出的商品数量"""
        return (
            self._session.query(
                model.Inventory.item_name,
                model.Inventory.brand,
                model.Batch.batch_serial_number,
                model.Batch.created_time,
                func.count(1),
                model.Inventory.return_times,
            )
            .join(model.Batch, model.Inventory.batch_id == model.Batch.id)
            .filter(model.Inventory.is_sold == 0)
            .group_by(
                model.Inventory.batch_id,
                model.Inventory.brand,
                model.Inventory.item_name,
            )
            .all()
        )

    def get_all_inventory_and_count_group_by_batch_brand_name(
        self,
    ) -> list[tuple[str, str, str, datetime, int, int]]:
        """获取所有的商品数量"""
        return (
            self._session.query(
                model.Inventory.item_name,
                model.Inventory.brand,
                model.Batch.batch_serial_number,
                model.Batch.created_time,
                func.count(1),
                model.Inventory.return_times,
            )
            .join(model.Batch, model.Inventory.batch_id == model.Batch.id)
            .group_by(
                model.Inventory.batch_id,
                model.Inventory.brand,
                model.Inventory.item_name,
            )
            .all()
        )


if __name__ == "__main__":
    from pprint import pprint

    g = GetAttributeService()
    # print(g.get_latest_batch_serial_number())
    # pprint(g.get_all_inventory_and_count_group_by_batch_brand_name())
    pprint(g.get_latest_batch_serial_number())
    pprint(g.get_latest_wave_serial_number())
