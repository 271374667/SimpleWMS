from datetime import date
from typing import Optional

from sqlalchemy import and_
from sqlalchemy.orm import Query

from src.common.database import Session
from src.common.database.entity import model
from typing import Tuple

class GetModelService:
    def __init__(self):
        self._session = Session

    # 基础查询
    def get_all_inventory(self) -> Query[model.Inventory]:
        return self._session.query(model.Inventory)

    def get_all_batch(self) -> Query[model.Batch]:
        return self._session.query(model.Batch)

    def get_all_wave(self) -> Query[model.Wave]:
        return self._session.query(model.Wave)

    def get_all_data(self) -> Query[Tuple[model.Inventory , model.Batch , model.Wave]]:
        return self._session.query(model.Inventory, model.Batch, model.Wave).join(model.Batch, isouter=True).join(model.Wave, isouter=True)

    # 通过属性查询
    def get_inventory_greater_than_id(self, id: int) -> Query[model.Inventory]:
        return self._session.query(model.Inventory).filter(model.Inventory.id > id)

    def get_inventory_by_ean13(self, ean13: str) -> Query[model.Inventory]:
        number = ean13[:12]
        return self._session.query(model.Inventory).filter(model.Inventory.id == int(number))

    def get_wave_by_serial_number(self, serial_number: str) -> Query[model.Wave]:
        return self._session.query(model.Wave).filter(model.Wave.wave_serial_number == serial_number)

    def get_batch_by_serial_number(self, serial_number: str) -> Query[model.Batch]:
        return self._session.query(model.Batch).filter(model.Batch.batch_serial_number == serial_number)

    # 按照时间进行获取
    # TODO: 这里的时间都必须要高度抽象，之后要改成两个时间参数获取值,比如start_datetime, end_datetime
    def get_all_inventory_by_date(self,
                                  start_time: Optional[date] = None,
                                  end_time: Optional[date] = None
                                  ) -> Query[model.Inventory]:
        """根据时间来获取商品

        根据时间来获取商品,如果没有传入时间参数,则默认获取本月的商品

        Args:
            start_time: 开始时间
            end_time: 结束时间

        Returns:
            Query: 查询结果,该结果需要使用 .all() 方法来获取所有的结果,或者可以继续进行查询
        """
        if start_time is None and end_time is None:
            today = date.today()
            return self._session.query(model.Inventory).filter(model.Inventory.batch.has(
                    model.Batch.created_time >= today.replace(day=1)))

        elif start_time is not None and end_time is not None:
            return self._session.query(model.Inventory).filter(
                    and_(
                            model.Inventory.batch.has(model.Batch.created_time >= start_time),
                            model.Inventory.batch.has(model.Batch.created_time <= end_time)
                            )
                    )
        elif start_time is not None:
            return self._session.query(model.Inventory).filter(
                    model.Inventory.batch.has(model.Batch.created_time >= start_time)
                    )
        else:
            return self._session.query(model.Inventory).filter(
                    model.Inventory.batch.has(model.Batch.created_time <= end_time)
                    )

    def get_all_batch_by_date(self,
                              start_time: Optional[date] = None,
                              end_time: Optional[date] = None
                              ) -> Query[model.Batch]:
        """根据时间来获取商品

        根据时间来获取批次,如果没有传入时间参数,则默认获取本月的批次

        Args:
            start_time: 开始时间
            end_time: 结束时间

        Returns:
            Query: 查询结果,该结果需要使用 .all() 方法来获取所有的结果,或者可以继续进行查询
        """
        if start_time is None and end_time is None:
            today = date.today()
            return self._session.query(model.Batch).filter(model.Batch.created_time >= today.replace(day=1))
        elif start_time is not None and end_time is not None:
            return self._session.query(model.Batch).filter(
                    and_(
                            model.Batch.created_time >= start_time,
                            model.Batch.created_time <= end_time
                            )
                    )
        elif start_time is not None:
            return self._session.query(model.Batch).filter(model.Batch.created_time >= start_time)
        else:
            return self._session.query(model.Batch).filter(model.Batch.created_time <= end_time)

    def get_all_wave_by_date(self,
                             start_time: Optional[date] = None,
                             end_time: Optional[date] = None
                             ) -> Query[model.Wave]:
        """根据时间来获取波次

        根据时间来获取批次,如果没有传入时间参数,则默认获取本月的批次

        Args:
            start_time: 开始时间
            end_time: 结束时间

        Returns:
            Query: 查询结果,该结果需要使用 .all() 方法来获取所有的结果,或者可以继续进行查询
        """
        if start_time is None and end_time is None:
            today = date.today()
            return self._session.query(model.Wave).filter(model.Wave.created_time >= today.replace(day=1))
        elif start_time is not None and end_time is not None:
            return self._session.query(model.Wave).filter(
                    and_(
                            model.Wave.created_time >= start_time,
                            model.Wave.created_time <= end_time
                            )
                    )
        elif start_time is not None:
            return self._session.query(model.Wave).filter(model.Wave.created_time >= start_time)
        else:
            return self._session.query(model.Wave).filter(model.Wave.created_time <= end_time)

    # 按照是否售出进行获取
    def get_unsold_inventory(self) -> Query[model.Inventory]:
        """获取未售出的商品数量"""
        return (
                self._session.query(model.Inventory)
                .filter(model.Inventory.is_sold == 0)
        )

    def get_unsold_inventory_this_month(self) -> Query[model.Inventory]:
        """获取本月未售出的商品数量"""
        today = date.today()
        return (
                self._session.query(model.Inventory)
                .filter(
                        and_(
                                model.Inventory.is_sold == 0,
                                model.Inventory.batch.has(
                                        model.Batch.created_time >= today.replace(day=1)
                                        ),
                                )
                        )
        )


if __name__ == '__main__':
    from pprint import pprint

    g = GetModelService()
    a = g.get_all_data()
    a.filter(model.Inventory.price > 0)
    # a.filter_by(model.Inventory.price > 0)
    a = a.all()
    pprint(len(a))
    # pprint(a[0].price)
    # pprint(g.get_all_data().first())
