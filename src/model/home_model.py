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
