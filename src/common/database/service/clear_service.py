import loguru

from src.common.database import get_session
from src.common.database.entity import model


class ClearService:
    def __init__(self):
        self._session = get_session()

    def clear_all(self) -> None:
        # 只清除其中的数据,不清除表
        self.clear_wave()
        self.clear_batch()
        self.clear_inventory()

        loguru.logger.success("清空数据库完成")

    def clear_inventory(self) -> None:
        self._session.query(model.Inventory).delete()
        self._session.commit()
        loguru.logger.success("清空库存完成")

    def clear_batch(self) -> None:
        self._session.query(model.Batch).delete()
        self._session.commit()
        loguru.logger.success("清空批次完成")

    def clear_wave(self) -> None:
        self._session.query(model.Wave).delete()
        self._session.commit()
        loguru.logger.success("清空波次完成")


if __name__ == "__main__":
    clear_service = ClearService()
    clear_service.clear_all()
