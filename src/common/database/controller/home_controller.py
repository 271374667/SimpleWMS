from src.common.database.service.get_model_service import GetModelService
from src.common.database.service.get_attribute_service import GetAttributeService
from src.common.database.utils import convert


class HomeController:
    def __init__(self):
        self._get_model_service = GetModelService()
        self._get_attribute_service = GetAttributeService()

    def get_current_batch_name(self) -> str:
        return convert.BatchConverter.convert_batch_serial_number_to_batch_name(self._get_attribute_service.get_latest_batch_serial_number())

    def get_current_wave_name(self) -> str:
        return convert.WaveConverter.convert_wave_serial_number_to_wave_name(self._get_attribute_service.get_latest_wave_serial_number())

    def get_current_item_quantity(self) -> int:
        return len(self._get_model_service.get_unsold_inventory_this_month())

    def get_current_money(self) -> int:
        inventory_this_month = self._get_model_service.get_unsold_inventory_this_month()
        return sum([x.price for x in inventory_this_month])

    def get_current_storage(self) -> int:
        return len(self._get_model_service.get_all_inventory_this_month())

    def get_current_retrieval(self) -> int:
        return len(self._get_model_service.get_all_inventory_this_month()) - len(
                self._get_model_service.get_unsold_inventory_this_month())

    def get_all_batch_number(self) -> int:
        return len(self._get_model_service.get_all_batch())

    def get_all_wave_number(self) -> int:
        return len(self._get_model_service.get_all_wave())

    def get_all_item_quantity(self) -> int:
        return len(self._get_model_service.get_all_inventory())

    def get_all_money(self) -> int:
        return sum([x.price for x in self._get_model_service.get_all_inventory()])

    def get_all_storage(self) -> int:
        return len(self._get_model_service.get_all_inventory())

    def get_all_retrieval(self) -> int:
        return len(self._get_model_service.get_all_inventory()) - len(self._get_model_service.get_unsold_inventory())
