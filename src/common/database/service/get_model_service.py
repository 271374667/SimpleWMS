from datetime import date
from typing import Tuple

from sqlalchemy.orm import Query

from src.common.database import Session
from src.common.database.entity import model


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

    def get_all_data(self) -> Query[Tuple[model.Inventory, model.Batch, model.Wave]]:
        return (
            self._session.query(model.Inventory, model.Batch, model.Wave)
            .join(model.Batch, isouter=True)
            .join(model.Wave, isouter=True)
        )

    def get_custom_query(self, *query_list) -> Query:
        return self._session.query(*query_list)


if __name__ == "__main__":
    from pprint import pprint

    g = GetModelService()
    a = g.get_all_batch()
    pprint(a.filter(model.Batch.created_time <= date.today()).all())
