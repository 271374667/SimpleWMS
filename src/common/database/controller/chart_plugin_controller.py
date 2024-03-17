from datetime import date
from typing import List, Tuple
from typing import Literal, Optional

from sqlalchemy import func

from src.common.database.entity import model
from src.common.database.query_filter import (
    AttrFilter,
    GroupByFilter,
    TimeFilter,
    TimeFilterEnum,
)
from src.common.database.service.get_attribute_service import (
    GetAttributeService,
    GetModelService,
)


class ChartPluginController:
    def __init__(self):
        self._get_attribute_service = GetAttributeService()
        self._get_model_service = GetModelService()

    def get_count_groupby_brand(
        self,
        is_sold: Literal[0, 1] = 0,
        statistic_time: Optional[TimeFilterEnum] = None,
        start_time: Optional[date] = None,
        end_time: Optional[date] = None,
    ) -> List[Tuple[str, int]]:
        """获取品牌数量"""
        count = func.count(1)
        query = self._get_model_service.get_custom_query(model.Inventory.brand, count)
        query = AttrFilter.inventory_is_sold(query, is_sold)  # 统计未卖出的

        if statistic_time is not None or start_time is not None or end_time is not None:
            query = TimeFilter.inventory_created_time(
                query,
                time_filter_enum=statistic_time,
                start_time=start_time,
                end_time=end_time,
            )

        query = GroupByFilter.brand(query)
        query.order_by(count.desc())
        return query.all()


if __name__ == "__main__":
    controller = ChartPluginController()
