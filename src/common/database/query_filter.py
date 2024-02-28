from datetime import date, datetime, timedelta
from typing import Literal, Optional

from sqlalchemy import and_
from sqlalchemy.orm import Query

from src.common.database.entity import model
from src.enums import TimeFilterEnum


class GroupByFilter(Query):
    @staticmethod
    def brand(query: Query) -> Query:
        return query.group_by(model.Inventory.brand)

    @staticmethod
    def brand_and_name(query: Query) -> Query:
        return query.group_by(model.Inventory.brand, model.Inventory.item_name)

    @staticmethod
    def custom_group_by(query: Query, group_by_query: list) -> Query:
        return query.group_by(*group_by_query)


class IdFilter(Query):
    """
    这里的 Id 是通指
    能确定物品唯一性的都是 Id, inventory.id, ean13, batch_serial_number, wave_serial_number 等等
    """

    @staticmethod
    def inventory_id_greater_than(query: Query, id: int) -> Query:
        return query.filter(model.Inventory.id > id)

    @staticmethod
    def inventory_ean13(query: Query, ean13: str) -> Query:
        number = ean13[:12]
        return query.filter(model.Inventory.id == int(number))

    @staticmethod
    def batch_serial_number(query: Query, serial_number: str) -> Query:
        return query.filter(model.Batch.batch_serial_number == serial_number)

    @staticmethod
    def wave_serial_number(query: Query, serial_number: str) -> Query:
        return query.filter(model.Wave.wave_serial_number == serial_number)


class TimeFilter(Query):
    """
    一般情况下没法直接用 datetime 和 date 来比较, 但是在 sqlalchemy 里面好像做了处理,所以可以直接比较
    于是为了方便,这里直接使用 date 类型
    """

    @staticmethod
    def inventory_created_time(query: Query,
                               start_time: Optional[date] = None,
                               end_time: Optional[date] = None,
                               time_filter_enum: Optional[TimeFilterEnum] = None) -> Query:
        """
        通过时间筛选 Inventory
        Args:
            query: sqlchemy的查询对象
            start_time: 开始时间
            end_time: 结束时间
            time_filter_enum: 常用时间类型

        Returns:
            sqlalchemy 的查询对象,之后可以继续链式调用
        """

        today = date.today()

        # 如果有time_filter_enum参数则优先使用time_filter_enum参数
        if time_filter_enum is None:
            # 如果没有time_filter_enum参数则使用start_time和end_time参数
            if start_time is None and end_time is None:
                return query

            elif start_time is not None and end_time is not None:
                return query.filter(
                        and_(
                                model.Inventory.batch.has(model.Batch.created_time >= start_time),
                                model.Inventory.batch.has(model.Batch.created_time <= end_time)
                                )
                        )
            elif start_time is not None:
                return query.filter(
                        model.Inventory.batch.has(model.Batch.created_time >= start_time)
                        )
            else:
                return query.filter(
                        model.Inventory.batch.has(model.Batch.created_time <= end_time)
                        )

        elif time_filter_enum == TimeFilterEnum.Day:
            return query.filter(model.Inventory.batch.has(model.Batch.created_time >= today))
        elif time_filter_enum == TimeFilterEnum.Week:
            temp_time = today - timedelta(days=7)
            return query.filter(model.Inventory.batch.has(model.Batch.created_time >= temp_time))
        elif time_filter_enum == TimeFilterEnum.FiftenDays:
            temp_time = today - timedelta(days=15)
            return query.filter(model.Inventory.batch.has(model.Batch.created_time >= temp_time))
        elif time_filter_enum == TimeFilterEnum.Month:
            temp_time = today - timedelta(days=30)
            return query.filter(model.Inventory.batch.has(model.Batch.created_time >= temp_time))
        elif time_filter_enum == TimeFilterEnum.All:
            return query
        else:
            raise ValueError("time_filter_enum 参数错误")

    @staticmethod
    def batch_created_time(query: Query,
                           start_time: Optional[date] = None,
                           end_time: Optional[date] = None,
                           time_filter_enum: Optional[TimeFilterEnum] = None) -> Query:
        """
        通过时间筛选 batch
        Args:
            query: sqlchemy的查询对象
            start_time: 开始时间
            end_time: 结束时间
            time_filter_enum: 常用时间类型

        Returns:
            sqlalchemy 的查询对象,之后可以继续链式调用
        """
        today = date.today()

        # 如果有time_filter_enum参数则优先使用time_filter_enum参数
        if time_filter_enum is None:
            # 如果没有time_filter_enum参数则使用start_time和end_time参数
            if start_time is None and end_time is None:
                return query

            elif start_time is not None and end_time is not None:
                return query.filter(
                        and_(
                                model.Batch.created_time >= start_time,
                                model.Batch.created_time <= end_time
                                )
                        )
            elif start_time is not None:
                return query.filter(model.Batch.created_time >= start_time)
            else:
                return query.filter(model.Batch.created_time <= end_time)

        elif time_filter_enum == TimeFilterEnum.Day:
            return query.filter(model.Batch.created_time >= today)
        elif time_filter_enum == TimeFilterEnum.Week:
            temp_time = today - timedelta(days=7)
            return query.filter(model.Batch.created_time >= temp_time)
        elif time_filter_enum == TimeFilterEnum.FiftenDays:
            temp_time = today - timedelta(days=15)
            return query.filter(model.Batch.created_time >= temp_time)
        elif time_filter_enum == TimeFilterEnum.Month:
            temp_time = today - timedelta(days=30)
            return query.filter(model.Batch.created_time >= temp_time)
        elif time_filter_enum == TimeFilterEnum.All:
            return query
        else:
            raise ValueError("time_filter_enum 参数错误")

    @staticmethod
    def wave_created_time(query: Query,
                          start_time: Optional[date] = None,
                          end_time: Optional[date] = None,
                          time_filter_enum: Optional[TimeFilterEnum] = None) -> Query:
        """
        通过时间筛选 wave
        Args:
            query: sqlchemy的查询对象
            start_time: 开始时间
            end_time: 结束时间
            time_filter_enum: 常用时间类型

        Returns:
            sqlalchemy 的查询对象,之后可以继续链式调用
        """
        today = date.today()

        # 如果有time_filter_enum参数则优先使用time_filter_enum参数
        if time_filter_enum is None:
            # 如果没有time_filter_enum参数则使用start_time和end_time参数
            if start_time is None and end_time is None:
                return query

            elif start_time is not None and end_time is not None:
                return query.filter(
                        and_(
                                model.Wave.created_time >= start_time,
                                model.Wave.created_time <= end_time
                                )
                        )
            elif start_time is not None:
                return query.filter(model.Wave.created_time >= start_time)
            else:
                return query.filter(model.Wave.created_time <= end_time)

        elif time_filter_enum == TimeFilterEnum.Day:
            return query.filter(model.Wave.created_time >= today)
        elif time_filter_enum == TimeFilterEnum.Week:
            temp_time = today - timedelta(days=7)
            return query.filter(model.Wave.created_time >= temp_time)
        elif time_filter_enum == TimeFilterEnum.FiftenDays:
            temp_time = today - timedelta(days=15)
            return query.filter(model.Wave.created_time >= temp_time)
        elif time_filter_enum == TimeFilterEnum.Month:
            temp_time = today - timedelta(days=30)
            return query.filter(model.Wave.created_time >= temp_time)
        elif time_filter_enum == TimeFilterEnum.All:
            return query
        else:
            raise ValueError("time_filter_enum 参数错误")


class AttrFilter(Query):
    @staticmethod
    def inventory_brand(query: Query, brand: str) -> Query:
        return query.filter(model.Inventory.brand == brand)

    @staticmethod
    def inventory_item_name(query: Query, item_name: str) -> Query:
        return query.filter(model.Inventory.item_name == item_name)

    @staticmethod
    def inventory_is_sold(query: Query, is_sold: Literal[0, 1]) -> Query:
        """根据是否售出进行筛选, 0 未售出, 1 已售出"""
        return query.filter(model.Inventory.is_sold == is_sold)

    @staticmethod
    def batch_batch_serial_number(query: Query, batch_serial_number: str) -> Query:
        return query.filter(model.Batch.batch_serial_number == batch_serial_number)

    @staticmethod
    def wave_wave_serial_number(query: Query, wave_serial_number: str) -> Query:
        return query.filter(model.Wave.wave_serial_number == wave_serial_number)


if __name__ == '__main__':
    print(datetime.now() > date(2021, 1, 1))
