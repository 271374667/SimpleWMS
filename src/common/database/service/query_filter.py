from sqlalchemy.orm import Query

from src.common.database.entity import model


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
