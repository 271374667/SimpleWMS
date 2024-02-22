from src import dict_typing
from src.common.database.controller.home_controller import HomeController


class HomeModel:
    def __init__(self):
        self._db_controller = HomeController()

    def get_current_batch_name(self) -> str:
        return self._db_controller.get_current_batch_name()

    def get_current_wave_name(self) -> str:
        return self._db_controller.get_current_wave_name()

    def get_current_item_quantity(self) -> int:
        return self._db_controller.get_current_item_quantity()

    def get_current_money(self) -> int:
        return self._db_controller.get_current_money()

    def get_current_storage(self) -> int:
        return self._db_controller.get_current_storage()

    def get_current_retrieval(self) -> int:
        return self._db_controller.get_current_retrieval()

    def get_all_batch_number(self) -> int:
        return self._db_controller.get_all_batch_number()

    def get_all_wave_number(self) -> int:
        return self._db_controller.get_all_wave_number()

    def get_all_item_quantity(self) -> int:
        return self._db_controller.get_all_item_quantity()

    def get_all_money(self) -> int:
        return self._db_controller.get_all_money()

    def get_all_storage(self) -> int:
        return self._db_controller.get_all_storage()

    def get_all_retrieval(self) -> int:
        return self._db_controller.get_all_retrieval()

    # 下面是点击 card 之后出现的表格的数据
    def get_current_batch_card_data(self) -> list[dict_typing.BatchCardDict]:
        return self._db_controller.get_current_batch_card_data()

    def get_all_batch_card_data(self) -> list[dict_typing.BatchCardDict]:
        return self._db_controller.get_all_batch_card_data()

    def get_current_wave_card_data(self) -> list[dict_typing.WaveCardDict]:
        return self._db_controller.get_current_wave_card_data()

    def get_all_wave_card_data(self) -> list[dict_typing.WaveCardDict]:
        return self._db_controller.get_all_wave_card_data()

    def get_current_item_quantity_card_data(self) -> list[dict_typing.ItemQuantityCardDict]:
        return self._db_controller.get_current_item_quantity_card_data()

    def get_all_item_quantity_card_data(self) -> list[dict_typing.ItemQuantityCardDict]:
        return self._db_controller.get_all_item_quantity_card_data()

    def get_current_money_card_data(self) -> list[dict_typing.MoneyCardDict]:
        return self._db_controller.get_current_money_card_data()

    def get_all_money_card_data(self) -> list[dict_typing.MoneyCardDict]:
        return self._db_controller.get_all_money_card_data()

    def get_current_storage_card_data(self) -> list[dict_typing.StorageCardDict]:
        return self._db_controller.get_current_storage_card_data()

    def get_all_storage_card_data(self) -> list[dict_typing.StorageCardDict]:
        return self._db_controller.get_all_storage_card_data()

    def get_current_retrieval_card_data(self) -> list[dict_typing.RetrievalCardDict]:
        return self._db_controller.get_current_retrieval_card_data()

    def get_all_retrieval_card_data(self) -> list[dict_typing.RetrievalCardDict]:
        return self._db_controller.get_all_retrieval_card_data()
