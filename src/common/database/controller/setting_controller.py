from typing import List

from src.common.database.service.get_model_service import GetModelService
from src.common.database.utils import convert
from src.dict_typing import AllInventoryDict


class SettingController:
    def __init__(self):
        self._get_model_service = GetModelService()

    def export_database(self) -> List[AllInventoryDict]:
        data = self._get_model_service.get_all_data().all()
        result: List[AllInventoryDict] = []
        for inventory, batch, wave in data:
            result.append({
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
                    "is_wave_active": wave.is_active if wave else None
                    })
        return result


if __name__ == '__main__':
    from pprint import pprint

    setting_controller = SettingController()
    a = setting_controller.export_database()
    pprint(a)
