from datetime import datetime, timedelta
from typing import List, Optional, Tuple

from PySide6.QtCore import Qt
from sqlalchemy.orm import Query
from sqlalchemy.sql import sqltypes

from src.common.database.entity import model
from src.common.database.service.get_attribute_service import (
    GetAttributeService,
    GetModelService,
    )
from src.common.database.utils import convert
from src.core.dict_typing import (
    BasicSearchParameterDict,
    )
from src.core.enums import BasicSearchCombboxOperationEnum
from src.core.wms_dataclass import (
    BasicSearchDataclass,
    BasicSearchParameterDataclass,
    OutOfStockDataclass,
    ReturnTimesDataclass,
    UnsalableDataclass,
    )


class DatabasePluginController:
    def __init__(self):
        self._get_attribute_service = GetAttributeService()
        self._get_model_service = GetModelService()

    def get_unsalable_data(
        self, limit: Optional[int] = None, offset: Optional[int] = None
    ) -> List[UnsalableDataclass]:
        """获取滞销数据
        Returns:
            list[UnsalableDataclass]: 滞销数据
                [UnsalableDataclass(物品名称, 品牌, 批次, 在仓库中停留的天数, 存货数量, 总共进货, 存货率)]
        """
        total_data_after_group = self._get_attribute_service.get_all_inventory_and_count_group_by_batch_brand_name(
            limit=limit, offset=offset
        )
        unsold_data_after_group = self._get_attribute_service.get_unsold_inventory_and_count_group_by_batch_brand_name(
            limit=limit, offset=offset
        )
        today = datetime.now()

        # 根据未销售的数据进行计算
        unsold_data: list[UnsalableDataclass] = []
        for unsold in unsold_data_after_group:
            for total in total_data_after_group:
                if (
                    unsold[0] == total[0]
                    and unsold[1] == total[1]
                    and unsold[2] == total[2]
                ):
                    # 获取在仓库中停留的天数
                    stay_days = (today.date() - total[3].date()).days
                    unsold_data.append(
                        UnsalableDataclass(
                            商品名称=unsold[0],
                            品牌名称=unsold[1],
                            批次编号=unsold[2],
                            入库天数=stay_days,
                            库存量=unsold[4],
                            总数=total[4],
                            存货率=round((unsold[4] / total[4]), 6) * 100,
                        )
                    )
        return unsold_data

    def get_out_of_stock_data(
        self, limit: Optional[int] = None, offset: Optional[int] = None
    ) -> List[OutOfStockDataclass]:
        """获取脱销数据
        因为脱销和滞销的计算逻辑是一样的,所以这里直接调用滞销的方法
        Returns:
            list[UnsalableDataclass]: 脱销数据
                [UnsalableDataclass(物品名称, 品牌, 批次, 在仓库中停留的天数, 存货数量, 总共进货, 存货率)]
        """
        total_data_after_group = self._get_attribute_service.get_all_inventory_and_count_group_by_batch_brand_name(
            limit=limit, offset=offset
        )
        out_of_stock_data_after_group = self._get_attribute_service.get_unsold_inventory_and_count_group_by_batch_brand_name(
            limit=limit, offset=offset
        )
        today = datetime.now()

        # 根据未销售的数据进行计算
        out_of_stock_data: list[OutOfStockDataclass] = []
        for out_of_stock in out_of_stock_data_after_group:
            for total in total_data_after_group:
                if (
                    out_of_stock[0] == total[0]
                    and out_of_stock[1] == total[1]
                    and out_of_stock[2] == total[2]
                ):
                    # 获取在仓库中停留的天数
                    stay_days = (today.date() - total[3].date()).days
                    out_of_stock_data.append(
                        OutOfStockDataclass(
                            商品名称=out_of_stock[0],
                            品牌名称=out_of_stock[1],
                            批次编号=out_of_stock[2],
                            入库天数=stay_days,
                            库存量=out_of_stock[4],
                            总数=total[4],
                            存货率=round((out_of_stock[4] / total[4]), 6) * 100,
                        )
                    )
        return out_of_stock_data

    def get_return_data(
        self, limit: Optional[int] = None, offset: Optional[int] = None
    ) -> list[ReturnTimesDataclass]:
        """获取退货数据"""
        # 获取所有数据
        # ['id', '商品名称', '品牌', '批次号', '入库时间', '退货次数', '退货率']

        query = self._get_model_service.get_custom_query(
            model.Inventory.id,
            model.Inventory.item_name,
            model.Inventory.brand,
            model.Inventory.batch_id,
            model.Batch.created_time,
            model.Inventory.return_times,
        )
        query = query.join(model.Batch, model.Inventory.batch_id == model.Batch.id)
        query = query.order_by(model.Inventory.return_times.desc())
        query = query.filter(model.Inventory.return_times > 0)
        query = query.limit(limit).offset(offset)
        data = query.all()
        if not data:
            return []

        # 将上面的数据转换成下面的数据['商品名称', '品牌', '批次号', '入库时间', '退货次数', 'EAN13']
        return_data: list[ReturnTimesDataclass] = []
        return_data.extend(
            ReturnTimesDataclass(
                商品名称=row[1],
                品牌名称=row[2],
                批次编号=row[3],
                入库时间=row[4],
                退货次数=row[5],
                Ean13码=convert.EAN13Converter.convert_id_to_ean13(row[3]),
            )
            for row in data
        )
        return return_data

    def get_basic_search_data(
        self,
        parameter: BasicSearchParameterDataclass,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
    ) -> List[BasicSearchDataclass]:
        """获取基础搜索数据"""
        # 获取所有数据
        # ['商品名称', '品牌', '批次号', '入库时间', '存库天数', '退货次数', '波次编号', '出库时间', '是否售出', 'EAN13']
        all_data = self._modify_query_based_on_conditions(
            parameter, limit, offset
        ).all()

        today = datetime.now()

        return [
            BasicSearchDataclass(
                Ean13码=convert.EAN13Converter.convert_id_to_ean13(each[0].id),
                商品名称=str(each[0].item_name),
                品牌名称=str(each[0].brand),
                价格=each[0].price,
                批次编号=str(each[1].batch_serial_number),
                入库时间=each[1].created_time,
                入库天数=(today - each[1].created_time).days,
                退货次数=each[0].return_times,
                波次编号=str(each[2].wave_serial_number if each[2] else ""),
                出库时间=each[2].created_time if each[2] else None,
                是否售出=bool(each[0].is_sold),
            )
            for each in all_data
        ]

    def get_basic_search_total(self, parameter: BasicSearchParameterDataclass) -> int:
        """获取基础搜索的总数"""
        query = self._modify_query_based_on_conditions(parameter)
        return query.count()

    def _modify_query_based_on_conditions(
        self,
        parameter: BasicSearchParameterDataclass,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
    ) -> Query[Tuple[model.Inventory, model.Batch, model.Wave]]:
        """根据条件修改查询"""
        all_data = (
            self._get_model_service.get_all_data()
        )  # [model.Inventory, model.Batch, model.Wave]
        if parameter.ean13:
            all_data = all_data.filter(
                model.Inventory.id
                == convert.EAN13Converter.convert_ean13_to_id(parameter.ean13)
            )
        if parameter.name:
            all_data = all_data.filter(
                model.Inventory.item_name.like(f"%{parameter.name}%")
            )
        if parameter.brand:
            all_data = all_data.filter(model.Inventory.brand == parameter.brand)
        if parameter.price_operation == BasicSearchCombboxOperationEnum.Equal:
            if parameter.has_price:
                all_data = all_data.filter(model.Inventory.price == parameter.price)
        elif parameter.price_operation == BasicSearchCombboxOperationEnum.Greater:
            if parameter.has_price:
                all_data = all_data.filter(model.Inventory.price > parameter.price)
        elif parameter.price_operation == BasicSearchCombboxOperationEnum.Less:
            if parameter.has_price:
                all_data = all_data.filter(model.Inventory.price < parameter.price)
        if parameter.batch_serial_number:
            all_data = all_data.filter(
                model.Inventory.batch_id == model.Batch.id
            ).filter(model.Batch.batch_serial_number == parameter.batch_serial_number)
        if parameter.wave_serial_number:
            all_data = all_data.filter(model.Inventory.wave_id == model.Wave.id).filter(
                model.Wave.wave_serial_number == parameter.wave_serial_number
            )
        # 根据存库天数搜索
        has_storage_days = parameter.has_storage_days
        storage_days = parameter.storage_days
        # 这里的逻辑比较复杂,因为create_time这个属性没有办法调用他的date(),所以只能提前获取今天的时间然后做比较
        if has_storage_days:
            today = datetime.now()
            storage_days_operation = parameter.storage_days_operation
            if storage_days_operation == BasicSearchCombboxOperationEnum.Equal:
                storage_days += (
                    1  # 一个bug,如果没有等于号实际上搜索结果为目标结果前一天
                )
                start_day = (today - timedelta(days=storage_days)).replace(
                    hour=0, minute=0, second=0
                )
                end_day = start_day.replace(hour=23, minute=59, second=59)
                all_data = (
                    all_data.filter(model.Inventory.batch_id == model.Batch.id)
                    .filter(start_day < model.Batch.created_time)
                    .filter(model.Batch.created_time < end_day)
                )

            elif storage_days_operation == BasicSearchCombboxOperationEnum.Greater:
                storage_days += (
                    1  # 一个bug,如果没有等于号实际上搜索结果为目标结果前一天
                )
                all_data = all_data.filter(
                    model.Inventory.batch_id == model.Batch.id
                ).filter(
                    model.Batch.created_time < today - timedelta(days=storage_days)
                )

            elif storage_days_operation == BasicSearchCombboxOperationEnum.Less:
                all_data = all_data.filter(
                    model.Inventory.batch_id == model.Batch.id
                ).filter(
                    model.Batch.created_time > today - timedelta(days=storage_days)
                )
        # 是否排序
        if parameter.has_sort:
            # 默认情况下传递的是字符串,需要转换成sqlalchemy的列类型
            sort_column_model = self._get_sort_column(parameter.sort_by)
            # Qt传入的是[升序, 降序]字符串,需要转换成Qt的枚举类型
            sort_order_qt = self._get_sort_order(parameter.sort_order)

            if sort_order_qt == Qt.SortOrder.AscendingOrder:
                all_data = all_data.order_by(sort_column_model)
            elif sort_order_qt == Qt.SortOrder.DescendingOrder:
                all_data = all_data.order_by(sort_column_model.desc())
        # 根据是否隐藏售出
        if parameter.hide_sold_item:
            all_data = all_data.filter(model.Inventory.is_sold == 0)
        # 是否隐藏有退货的
        if parameter.hide_has_return_item:
            all_data = all_data.filter(model.Inventory.return_times == 0)
        # 获取所有数据
        all_data = all_data.limit(limit).offset(offset)
        return all_data

    def _get_sort_column(self, sort_by: str) -> sqltypes:
        """将字符串转换成sqlalchemy的列类型"""
        str2model_dict = {
            "商品名称": model.Inventory.item_name,
            "品牌名称": model.Inventory.brand,
            "价格": model.Inventory.price,
            "批次编号": model.Batch.batch_serial_number,
            "入库时间": model.Batch.created_time,
            "入库天数": model.Batch.created_time,
            "退货次数": model.Inventory.return_times,
            "波次编号": model.Wave.wave_serial_number,
            "出库时间": model.Wave.created_time,
            "是否售出": model.Inventory.is_sold,
        }
        return str2model_dict.get(sort_by)

    def _get_sort_order(self, sort_order: str) -> Qt.SortOrder:
        """将字符串转换成sqlalchemy的列类型"""
        str2model_dict = {
            "升序": Qt.SortOrder.AscendingOrder,
            "降序": Qt.SortOrder.DescendingOrder,
        }
        return str2model_dict.get(sort_order)


if __name__ == "__main__":
    d = DatabasePluginController()
    # 测试一下get_basic_search_data
    parameter: BasicSearchParameterDict = {
        "name": "毛衣",
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
    # result = d.get_basic_search_data(parameter)
    #
    # session = get_session()
    #
    # result = session.query(model.Inventory)
    #
    # pprint(result)
    # pprint(result.all())
