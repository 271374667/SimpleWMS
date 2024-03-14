from datetime import datetime
from typing import Optional

from src.common.database import Session
from src.common.database.entity import model
from src.common.database.query_filter import IdFilter
from src.common.database.service.get_model_service import GetModelService


class AddModelService:
    def __init__(self):
        self._session = Session
        self._get_model_service = GetModelService()

    def add_one_record(self, inventory_model: model.Inventory,
                       batch_model: model.Batch,
                       wave_model: Optional[model.Wave] = None
                       ) -> None:
        """这个是为了导入数据库的时候用的,你需要先自己创建好批次和波次,然后再导入库存"""
        inventory_model.batch = batch_model
        if wave_model is not None:
            inventory_model.wave = wave_model
        self._session.add(inventory_model)
        self._session.commit()

    def add_many_records(self, inventory_models: list[model.Inventory]) -> None:
        self._session.add_all(inventory_models)
        self._session.commit()

    def add_inventory(self, item_name: str,
                      price: float,
                      brand: str,
                      batch: model.Batch,
                      id: Optional[int] = None,
                      is_active: Optional[int] = 1
                      ) -> model.Inventory:
        # 批次存在则获取批次，不存在则创建批次
        query = self._get_model_service.get_all_batch()
        query = IdFilter.batch_serial_number(query, batch.batch_serial_number)
        batch_sqlalchemy_model = query.first()
        if batch_sqlalchemy_model is None:
            batch_sqlalchemy_model = batch

        # MD一开始没想到需要备份导入数据库,想着不需要用到id和is_active,
        # 一开始没分离,现在为了省事直接用if判断
        if id is not None:
            inventory_sqlalchemy_model = model.Inventory(id=id,
                                                         item_name=item_name,
                                                         price=price,
                                                         brand=brand,
                                                         batch=batch_sqlalchemy_model,
                                                         is_active=is_active)
        else:
            inventory_sqlalchemy_model = model.Inventory(item_name=item_name,
                                                         price=price,
                                                         brand=brand,
                                                         batch=batch_sqlalchemy_model)
        return self.add_and_commit(inventory_sqlalchemy_model)

    def add_batch(self, batch_serial_number: str,
                  batch_name: str,
                  created_time: datetime,
                  id: Optional[int] = None,
                  is_active: Optional[int] = True
                  ) -> model.Batch:
        if id is not None:
            batch_sqlalchemy_model = model.Batch(batch_serial_number=batch_serial_number,
                                                 batch_name=batch_name,
                                                 created_time=created_time)
        else:
            batch_sqlalchemy_model = model.Batch(id=id,
                                                 batch_serial_number=batch_serial_number,
                                                 batch_name=batch_name,
                                                 created_time=created_time,
                                                 is_active=is_active)
        return self.add_and_commit(batch_sqlalchemy_model)

    def add_wave(self, wave_serial_number: str,
                 wave_name: str,
                 created_time: datetime,
                 id: Optional[int] = None,
                 is_active: Optional[int] = True
                 ) -> model.Wave:
        if id is not None:
            wave_sqlalchemy_model = model.Wave(wave_serial_number=wave_serial_number,
                                               wave_name=wave_name,
                                               created_time=created_time)
        else:
            wave_sqlalchemy_model = model.Wave(id=id,
                                               wave_serial_number=wave_serial_number,
                                               wave_name=wave_name,
                                               created_time=created_time,
                                               is_active=is_active)

        return self.add_and_commit(wave_sqlalchemy_model)

    def add_and_commit(self, new_model):
        # 其实我本来不想分出来的,但是Sourcery非要给我标波浪线,所以我就分出来了
        self._session.add(new_model)
        self._session.commit()
        return new_model
