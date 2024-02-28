from datetime import datetime

from sqlalchemy import func

from src import dict_typing
from src.common.database import Session
from src.common.database.entity import model
from src.common.database.query_filter import AttrFilter, TimeFilter, TimeFilterEnum
from src.common.database.service.get_attribute_service import GetAttributeService
from src.common.database.service.get_model_service import GetModelService
from src.common.database.utils import convert


class HomeController:
    def __init__(self):
        self._get_model_service = GetModelService()
        self._get_attribute_service = GetAttributeService()
        self._session = Session

    def get_current_batch_name(self) -> str:
        return convert.BatchConverter.convert_batch_serial_number_to_batch_name(
                self._get_attribute_service.get_latest_batch_serial_number())

    def get_current_wave_name(self) -> str:
        return convert.WaveConverter.convert_wave_serial_number_to_wave_name(
                self._get_attribute_service.get_latest_wave_serial_number())

    def get_current_item_quantity(self) -> int:
        query = self._get_model_service.get_all_inventory()
        query = TimeFilter.inventory_created_time(query, time_filter_enum=TimeFilterEnum.Month)
        query = AttrFilter.inventory_is_sold(query, 0)
        return len(query.all())

    def get_current_money(self) -> int:
        query = self._get_model_service.get_all_inventory()
        query = TimeFilter.inventory_created_time(query, time_filter_enum=TimeFilterEnum.Month)
        query = AttrFilter.inventory_is_sold(query, 0)
        inventory_this_month = query.all()
        return sum(x.price for x in inventory_this_month)

    def get_current_storage(self) -> int:
        query = self._get_model_service.get_all_inventory()
        query = TimeFilter.inventory_created_time(query, time_filter_enum=TimeFilterEnum.Month)
        return len(query.all())

    def get_current_retrieval(self) -> int:
        query1 = self._get_model_service.get_all_inventory()
        query1 = TimeFilter.inventory_created_time(query1, time_filter_enum=TimeFilterEnum.Month)

        query2 = self._get_model_service.get_all_inventory()
        query2 = TimeFilter.inventory_created_time(query2, time_filter_enum=TimeFilterEnum.Month)
        query2 = AttrFilter.inventory_is_sold(query2, 0)
        return len(query1.all()) - len(query2.all())

    def get_all_batch_number(self) -> int:
        return len(self._get_model_service.get_all_batch().all())

    def get_all_wave_number(self) -> int:
        return len(self._get_model_service.get_all_wave().all())

    def get_all_item_quantity(self) -> int:
        return len(self._get_model_service.get_all_inventory().all())

    def get_all_money(self) -> int:
        data = self._get_model_service.get_all_inventory().all()
        return sum(x.price for x in data)

    def get_all_storage(self) -> int:
        return len(self._get_model_service.get_all_inventory().all())

    def get_all_retrieval(self) -> int:
        query = self._get_model_service.get_all_inventory()
        query = AttrFilter.inventory_is_sold(query, 0)
        return len(self._get_model_service.get_all_inventory().all()) - len(
                query.all())

    # 下面是点击 card 之后出现的表格的数据
    def get_current_batch_card_data(self) -> list[dict_typing.BatchCardDict]:
        today = datetime.now()
        month_begin = datetime(today.year, today.month, 1)
        result = ((self._session
                   .query(model.Batch.batch_serial_number,
                          model.Batch.created_time,
                          func.count(1))
                   .join(model.Inventory, isouter=True)
                   .where(model.Batch.created_time >= month_begin)
                   .where(model.Inventory.is_sold == 0)
                   .group_by(model.Inventory.batch_id))
                  .order_by(model.Batch.created_time.desc()).all())
        result_dict: list[dict_typing.BatchCardDict] = []
        for r in result:
            result_dict.append(dict_typing.BatchCardDict(
                    batch_serial_number=r[0],
                    batch_created_time=r[1],
                    item_quantity=r[2]
                    ))
        return result_dict

    def get_all_batch_card_data(self) -> list[dict_typing.BatchCardDict]:
        result = ((self._session
                   .query(model.Batch.batch_serial_number,
                          model.Batch.created_time,
                          func.count(1))
                   .join(model.Inventory, isouter=True)
                   .group_by(model.Inventory.batch_id))
                  .order_by(model.Batch.created_time.desc()).all())
        result_dict: list[dict_typing.BatchCardDict] = []
        for r in result:
            result_dict.append(dict_typing.BatchCardDict(
                    batch_serial_number=r[0],
                    batch_created_time=r[1],
                    item_quantity=r[2]
                    ))
        return result_dict

    def get_current_wave_card_data(self) -> list[dict_typing.WaveCardDict]:
        today = datetime.now()
        month_begin = datetime(today.year, today.month, 1)
        result = ((self._session
                   .query(model.Wave.wave_serial_number,
                          model.Wave.created_time,
                          func.count(1))
                   .where(model.Wave.created_time >= month_begin)
                   .where(model.Inventory.is_sold == 1)
                   .join(model.Inventory, isouter=True)
                   .group_by(model.Inventory.wave_id))
                  .order_by(model.Wave.created_time.desc()).all())
        result_dict: list[dict_typing.WaveCardDict] = []
        for r in result:
            result_dict.append(dict_typing.WaveCardDict(
                    wave_serial_number=r[0],
                    wave_created_time=r[1],
                    item_quantity=r[2]
                    ))
        return result_dict

    def get_all_wave_card_data(self) -> list[dict_typing.WaveCardDict]:
        result = ((self._session
                   .query(model.Wave.wave_serial_number,
                          model.Wave.created_time,
                          func.count(1))
                   .join(model.Inventory, isouter=True)
                   .group_by(model.Inventory.wave_id))
                  .order_by(model.Wave.created_time.desc()).all())
        result_dict: list[dict_typing.WaveCardDict] = []
        for r in result:
            result_dict.append(dict_typing.WaveCardDict(
                    wave_serial_number=r[0],
                    wave_created_time=r[1],
                    item_quantity=r[2]
                    ))
        return result_dict

    def get_current_item_quantity_card_data(self) -> list[dict_typing.ItemQuantityCardDict]:
        today = datetime.now()
        month_begin = datetime(today.year, today.month, 1)

        result = (self._session.query(model.Inventory.item_name,
                                      model.Inventory.brand,
                                      func.count(1))
                  .join(model.Batch, isouter=True)
                  .where(model.Batch.created_time >= month_begin)
                  .where(model.Inventory.is_sold == 0)
                  .group_by(model.Inventory.item_name,
                            model.Inventory.brand)
                  .order_by(func.count(1).desc())
                  .all())
        result_dict: list[dict_typing.ItemQuantityCardDict] = []
        for r in result:
            result_dict.append(dict_typing.ItemQuantityCardDict(
                    name=r[0],
                    brand=r[1],
                    item_quantity=r[2]
                    ))
        return result_dict

    def get_all_item_quantity_card_data(self) -> list[dict_typing.ItemQuantityCardDict]:
        result = (self._session.query(model.Inventory.item_name,
                                      model.Inventory.brand,
                                      func.count(1))
                  .join(model.Batch, isouter=True)
                  .group_by(model.Inventory.item_name,
                            model.Inventory.brand)
                  .order_by(func.count(1).desc())
                  .all())
        result_dict: list[dict_typing.ItemQuantityCardDict] = []
        for r in result:
            result_dict.append(dict_typing.ItemQuantityCardDict(
                    name=r[0],
                    brand=r[1],
                    item_quantity=r[2]
                    ))
        return result_dict

    def get_current_money_card_data(self) -> list[dict_typing.MoneyCardDict]:
        today = datetime.now()
        month_begin = datetime(today.year, today.month, 1)
        result = (self._session.query(model.Inventory.item_name,
                                      model.Inventory.brand,
                                      func.sum(model.Inventory.price))
                  .join(model.Batch, isouter=True)
                  .where(model.Batch.created_time >= month_begin)
                  .where(model.Inventory.is_sold == 0)
                  .group_by(model.Inventory.item_name,
                            model.Inventory.brand)
                  .order_by(func.sum(model.Inventory.price).desc())
                  .all())
        result_dict: list[dict_typing.MoneyCardDict] = []
        for r in result:
            result_dict.append(dict_typing.MoneyCardDict(
                    name=r[0],
                    brand=r[1],
                    price=r[2]
                    ))
        return result_dict

    def get_all_money_card_data(self) -> list[dict_typing.MoneyCardDict]:
        result = (self._session.query(model.Inventory.item_name,
                                      model.Inventory.brand,
                                      func.sum(model.Inventory.price))
                  .join(model.Batch, isouter=True)
                  .group_by(model.Inventory.item_name,
                            model.Inventory.brand)
                  .order_by(func.sum(model.Inventory.price).desc())
                  .all())
        result_dict: list[dict_typing.MoneyCardDict] = []
        for r in result:
            result_dict.append(dict_typing.MoneyCardDict(
                    name=r[0],
                    brand=r[1],
                    price=r[2]
                    ))
        return result_dict

    def get_current_storage_card_data(self) -> list[dict_typing.StorageCardDict]:
        today = datetime.now()
        month_begin = datetime(today.year, today.month, 1)
        result = (self._session.query(model.Inventory.item_name,
                                      model.Inventory.brand,
                                      func.count(1))
                  .join(model.Batch, isouter=True)
                  .where(model.Batch.created_time >= month_begin)
                  .where(model.Inventory.is_sold == 0)
                  .group_by(model.Inventory.item_name,
                            model.Inventory.brand)
                  .order_by(func.count(1).desc())
                  .all())
        result_dict: list[dict_typing.StorageCardDict] = []
        for r in result:
            result_dict.append(dict_typing.StorageCardDict(
                    name=r[0],
                    brand=r[1],
                    storage_number=r[2]
                    ))
        return result_dict

    def get_all_storage_card_data(self) -> list[dict_typing.StorageCardDict]:
        result = (self._session.query(model.Inventory.item_name,
                                      model.Inventory.brand,
                                      func.count(1))
                  .join(model.Batch, isouter=True)
                  .where(model.Inventory.is_sold == 0)
                  .group_by(model.Inventory.item_name,
                            model.Inventory.brand)
                  .order_by(func.count(1).desc())
                  .all())
        result_dict: list[dict_typing.StorageCardDict] = []
        for r in result:
            result_dict.append(dict_typing.StorageCardDict(
                    name=r[0],
                    brand=r[1],
                    storage_number=r[2]
                    ))
        return result_dict

    def get_current_retrieval_card_data(self) -> list[dict_typing.RetrievalCardDict]:
        today = datetime.now()
        month_begin = datetime(today.year, today.month, 1)
        result = (self._session.query(model.Inventory.item_name,
                                      model.Inventory.brand,
                                      func.count(1))
                  .join(model.Batch, isouter=True)
                  .where(model.Batch.created_time >= month_begin)
                  .where(model.Inventory.is_sold == 1)
                  .group_by(model.Inventory.item_name,
                            model.Inventory.brand)
                  .order_by(func.count(1).desc())
                  .all())
        result_dict: list[dict_typing.RetrievalCardDict] = []
        for r in result:
            result_dict.append(dict_typing.RetrievalCardDict(
                    name=r[0],
                    brand=r[1],
                    retrieval_number=r[2]
                    ))
        return result_dict

    def get_all_retrieval_card_data(self) -> list[dict_typing.RetrievalCardDict]:
        result = (self._session.query(model.Inventory.item_name,
                                      model.Inventory.brand,
                                      func.count(1))
                  .join(model.Batch, isouter=True)
                  .where(model.Inventory.is_sold == 1)
                  .group_by(model.Inventory.item_name,
                            model.Inventory.brand)
                  .order_by(func.count(1).desc())
                  .all())
        result_dict: list[dict_typing.RetrievalCardDict] = []
        for r in result:
            result_dict.append(dict_typing.RetrievalCardDict(
                    name=r[0],
                    brand=r[1],
                    retrieval_number=r[2]
                    ))
        return result_dict


if __name__ == '__main__':
    from pprint import pprint

    h = HomeController()
    pprint(h.get_all_storage_card_data())
