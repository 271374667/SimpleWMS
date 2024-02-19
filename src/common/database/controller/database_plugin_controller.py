from datetime import datetime
from typing import List, Tuple

from src.common.database import get_session
from src.common.database.entity import model
from src.common.database.service.get_attribute_service import GetAttributeService
from src.common.database.utils import convert
from src.dict_typing import ReturnTimesDict, UnsalableDict


class DatabasePluginController:
    def __init__(self):
        self._get_attribute_service = GetAttributeService()
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


if __name__ == '__main__':
    from pprint import pprint

    # d = DatabasePluginController()
    # pprint(d.get_return_data())
    session = get_session()

    result = session.query(model.Inventory)

    result = result.filter(model.Inventory.return_times > 0)

    pprint(result)
    pprint(result.all())
