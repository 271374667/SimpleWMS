from typing import List

from src.common.database.entity.model import Batch, Inventory, Wave
from src.common.database.service.add_model_service import AddModelService
from src.common.database.service.clear_service import ClearService
from src.common.database.service.get_model_service import GetModelService
from src.common.database.utils import convert
from src.dict_typing import AllInventoryDict
from PySide6.QtCore import QObject, Signal


class SettingController(QObject):
    import_database_progress = Signal(float)

    def __init__(self):
        super().__init__()
        self._get_model_service = GetModelService()
        self._add_model_service = AddModelService()
        self._clear_service = ClearService()

    def export_database(self) -> List[AllInventoryDict]:
        data = self._get_model_service.get_all_data().all()
        result: List[AllInventoryDict] = []
        for inventory, batch, wave in data:
            result.append(
                {
                    "ean13": convert.EAN13Converter.convert_id_to_ean13(inventory.id),
                    "name": inventory.item_name,
                    "brand": inventory.brand,
                    "price": inventory.price,
                    "is_sold": inventory.is_sold,
                    "return_times": inventory.return_times,
                    "is_inventory_active": inventory.is_active,
                    "batch_id": batch.id,
                    "batch_name": batch.batch_name,
                    "batch_serial_number": batch.batch_serial_number,
                    "batch_created_time": batch.created_time,
                    "is_batch_active": batch.is_active,
                    "wave_id": wave.id if wave else None,
                    "wave_name": wave.wave_name if wave else None,
                    "wave_serial_number": wave.wave_serial_number if wave else None,
                    "wave_created_time": wave.created_time if wave else None,
                    "is_wave_active": wave.is_active if wave else None,
                }
            )
        return result

    def import_database(self, data: List[AllInventoryDict]) -> None:
        data_length = len(data)
        count: int = 0
        # 用字典来缓存,防止重复创建
        inventory_cache: list[Inventory] = []
        batch_cache: dict[str, Batch] = {}
        wave_cache: dict[str, Wave] = {}

        for item in data:
            count += 1
            self.import_database_progress.emit(count / data_length * 100)
            batch = Batch(
                id=item["batch_id"],
                batch_name=item["batch_name"],
                batch_serial_number=item["batch_serial_number"],
                created_time=item["batch_created_time"],
                is_active=item["is_batch_active"],
            )

            if item["batch_serial_number"] not in batch_cache:
                batch_cache[item["batch_serial_number"]] = batch

            inventory = Inventory(
                id=convert.EAN13Converter.convert_ean13_to_id(item["ean13"]),
                item_name=item["name"],
                price=item["price"],
                brand=item["brand"],
                is_sold=item["is_sold"],
                return_times=item["return_times"],
                is_active=item["is_inventory_active"],
            )

            if item["wave_id"]:
                wave = Wave(
                    id=item["wave_id"],
                    wave_name=item["wave_name"],
                    wave_serial_number=item["wave_serial_number"],
                    created_time=item["wave_created_time"],
                    is_active=item["is_wave_active"],
                )

                if item["wave_serial_number"] not in wave_cache:
                    wave_cache[item["wave_serial_number"]] = wave

                inventory.wave = wave_cache[item["wave_serial_number"]]
            inventory.batch = batch_cache[item["batch_serial_number"]]
            inventory_cache.append(inventory)
            self._add_model_service.add_many_records(inventory_cache)

    def clear_database(self) -> None:
        self._clear_service.clear_all()


if __name__ == "__main__":
    from pprint import pprint

    setting_controller = SettingController()
    a = setting_controller.export_database()
    pprint(a)
