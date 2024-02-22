from datetime import datetime, timedelta
from typing import List, Tuple

from src.common.database import get_session
from src.common.database.entity import model
from src.common.database.service.get_attribute_service import GetAttributeService, GetModelService
from src.common.database.utils import convert
from src.dict_typing import BasicSearchDict, BasicSearchParameterDict, ReturnTimesDict, UnsalableDict
from src.enums import BasicSearchCombboxOperationEnum


class DatabasePluginController:
    def __init__(self):
        self._get_attribute_service = GetAttributeService()
        self._get_model_service = GetModelService()
        self._session = get_session()

    def get_unsalable_data(self) -> List[UnsalableDict]:
        """获取滞销数据
        Returns:
            list[Tuple]: 滞销数据
                [(物品名称, 品牌, 批次, 在仓库中停留的天数, 存货数量, 总共进货, 存货率)]
        """
        total_data_after_group = self._get_attribute_service.get_all_inventory_and_count_group_by_batch_brand_name()
        unsold_data_after_group = self._get_attribute_service.get_unsold_inventory_and_count_group_by_batch_brand_name()
        today = datetime.now()

        # 根据未销售的数据进行计算
        unsold_data = []
        for unsold in unsold_data_after_group:
            for total in total_data_after_group:
                if unsold[0] == total[0] and unsold[1] == total[1] and unsold[2] == total[2]:
                    # 获取在仓库中停留的天数
                    stay_days = (today.date() - total[3].date()).days
                    unsold_data.append({
                            'name': unsold[0],
                            'brand': unsold[1],
                            'batch_serial_number': unsold[2],
                            'storage_time_from_today': stay_days,
                            'storage_count': unsold[4],
                            'total_count': total[4],
                            'storage_rate': round((unsold[4] / total[4]), 6) * 100
                            })
                    continue
        return unsold_data

    # 脱销的逻辑一样，这里直接偷懒
    get_out_of_stock_data = get_unsalable_data

    def get_return_data(self) -> list[ReturnTimesDict]:
        """获取退货数据"""
        # 获取所有数据
        # ['id', '商品名称', '品牌', '批次号', '入库时间', '退货次数', '退货率']

        data = (self._session.query(model.Inventory.id,
                                    model.Inventory.item_name,
                                    model.Inventory.brand,
                                    model.Inventory.batch_id,
                                    model.Batch.created_time,
                                    model.Inventory.return_times)
                .join(model.Batch, model.Inventory.batch_id == model.Batch.id)
                .order_by(model.Inventory.return_times.desc())
                .filter(model.Inventory.return_times > 0).all())
        if not data:
            return []

        # 将上面的数据转换成下面的数据['商品名称', '品牌', '批次号', '入库时间', '退货次数', 'EAN13']
        return_data = []
        for row in data:
            each_row: ReturnTimesDict = {
                    'name': row[1],
                    'brand': row[2],
                    'batch_serial_number': row[3],
                    'storage_time': row[4],
                    'return_times': row[5],
                    'ean13': convert.EAN13Converter.convert_id_to_ean13(row[3])
                    }
            return_data.append(each_row)
        return return_data

    def get_basic_search_data(self, parameter: BasicSearchParameterDict) -> List[BasicSearchDict]:
        """获取基础搜索数据"""
        # 获取所有数据
        # ['商品名称', '品牌', '批次号', '入库时间', '存库天数', '退货次数', '波次编号', '出库时间', '是否售出', 'EAN13']
        all_data = self._get_model_service.get_all_data()  # [model.Inventory, model.Batch, model.Wave]

        # 根据 ean13 搜索
        ean13 = parameter.get('ean13')
        if ean13:
            all_data = all_data.filter(model.Inventory.id == convert.EAN13Converter.convert_ean13_to_id(ean13))

        # 根据商品名称搜索
        name = parameter.get('name')
        if name:
            all_data = all_data.filter(model.Inventory.item_name.like(f'%{name}%'))

        # 根据品牌搜索
        brand = parameter.get('brand')
        if brand:
            all_data = all_data.filter(model.Inventory.brand == brand)

        # 根据价格搜索
        has_price = parameter.get('has_price')
        price = parameter.get('price')
        price_operation = parameter.get('price_operation')
        if has_price:
            if price_operation == BasicSearchCombboxOperationEnum.Equal:
                all_data = all_data.filter(model.Inventory.price == price)
            elif price_operation == BasicSearchCombboxOperationEnum.Greater:
                all_data = all_data.filter(model.Inventory.price > price)
            elif price_operation == BasicSearchCombboxOperationEnum.Less:
                all_data = all_data.filter(model.Inventory.price < price)

        # 根据批次号搜索
        batch_serial_number = parameter.get('batch_serial_number')
        if batch_serial_number:
            all_data = all_data.filter(model.Inventory.batch_id == model.Batch.id).filter(
                    model.Batch.batch_serial_number == batch_serial_number)

        # 根据波次号搜索
        wave_serial_number = parameter.get('wave_serial_number')
        if wave_serial_number:
            all_data = all_data.filter(model.Inventory.wave_id == model.Wave.id).filter(
                    model.Wave.wave_serial_number == wave_serial_number)

        # 根据存库天数搜索
        has_storage_days = parameter.get('has_storage_days')
        storage_days = parameter.get('storage_days')
        storage_days_operation = parameter.get('storage_days_operation')
        # 这里的逻辑比较复杂,因为create_time这个属性没有办法调用他的date(),所以只能提前获取今天的时间然后做比较
        if has_storage_days:
            today = datetime.now()
            if storage_days_operation == BasicSearchCombboxOperationEnum.Equal:
                storage_days += 1  # 一个bug,如果没有等于号实际上搜索结果为目标结果前一天
                start_day = (today - timedelta(days=storage_days)).replace(hour=0, minute=0, second=0)
                end_day = start_day.replace(hour=23, minute=59, second=59)
                all_data = (all_data.filter(model.Inventory.batch_id == model.Batch.id)
                            .filter(start_day < model.Batch.created_time)
                            .filter(model.Batch.created_time < end_day)
                            )

            elif storage_days_operation == BasicSearchCombboxOperationEnum.Greater:
                storage_days += 1  # 一个bug,如果没有等于号实际上搜索结果为目标结果前一天
                all_data = all_data.filter(model.Inventory.batch_id == model.Batch.id).filter(
                        model.Batch.created_time < today - timedelta(days=storage_days))

            elif storage_days_operation == BasicSearchCombboxOperationEnum.Less:
                all_data = all_data.filter(model.Inventory.batch_id == model.Batch.id).filter(
                        model.Batch.created_time > today - timedelta(days=storage_days))

        # 是否隐藏已经卖出的商品
        hide_sold_item = parameter.get('hide_sold_item')
        if hide_sold_item:
            all_data = all_data.filter(model.Inventory.is_sold == 0)

        # 是否隐藏已经退货的商品
        hide_has_return_item = parameter.get('hide_has_return_item')
        if hide_has_return_item:
            all_data = all_data.filter(model.Inventory.return_times == 0)

        # 获取所有数据
        all_data = all_data.all()

        result: list[BasicSearchDict] = []
        today = datetime.now()
        for each in all_data:
            result.append({
                    'name': str(each[0].item_name),
                    'brand': str(each[0].brand),
                    'price': each[0].price,
                    'batch_serial_number': str(each[1].batch_serial_number),
                    'storage_time': each[1].created_time,
                    'storage_time_from_today': (today - each[1].created_time).days,
                    'return_times': each[0].return_times,
                    'wave_serial_number': str(each[2].wave_serial_number if each[2] else ''),
                    'retrieval_time': each[2].created_time if each[2] else '',
                    'is_sold': '是' if each[0].is_sold else '否',
                    'ean13': convert.EAN13Converter.convert_id_to_ean13(each[0].id)
                    })
        return result


if __name__ == '__main__':
    from pprint import pprint

    d = DatabasePluginController()
    # 测试一下get_basic_search_data
    parameter: BasicSearchParameterDict = {
            'name': '毛衣',
            # 'brand': 'Nike',
            # 'has_price': True,
            # 'price': 300,
            # 'price_operation': BasicSearchCombboxOperationEnum.Greater,
            # 'batch_serial_number': 'test',
            # 'wave_serial_number': 'test',
            # 'has_storage_days': True,
            # 'storage_days': 16,
            # 'storage_days_operation': BasicSearchCombboxOperationEnum.Greater,
            # 'hide_sold_item': False,
            # 'hide_has_return_item': False
            }
    result = d.get_basic_search_data(parameter)
    pprint(result)
    pprint(len(result))
    #
    # session = get_session()
    #
    # result = session.query(model.Inventory)
    #
    # pprint(result)
    # pprint(result.all())
