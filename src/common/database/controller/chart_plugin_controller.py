from typing import List, Tuple

from sqlalchemy import func

from src.common.database.entity import model
from src.common.database.service.get_attribute_service import GetAttributeService, GetModelService
from src.common.database.query_filter import GroupByFilter


class ChartPluginController:
    def __init__(self):
        self._get_attribute_service = GetAttributeService()
        self._get_model_service = GetModelService()

    def get_count_groupby_brand(self) -> List[Tuple[str, int]]:
        """获取品牌数量"""
        query = self._get_model_service.get_custom_query(model.Inventory.brand, func.count(1))
        query = GroupByFilter.brand(query)
        return query.all()


if __name__ == '__main__':
    controller = ChartPluginController()
    print(controller.get_count_groupby_brand())
