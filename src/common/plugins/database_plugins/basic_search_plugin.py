from PySide6.QtWidgets import QWidget

from src.common.database.controller.database_plugin_controller import (
    DatabasePluginController,
)
from src.common.plugins.plugin_base import DatabasePluginBase
from src.dict_typing import BasicSearchDict, BasicSearchParameterDict
from src.enums import BasicSearchCombboxOperationEnum
from src.view.component_view.basic_search_plugin_component_view import (
    BasicSearchPluginComponentView,
)


class BasicSearchPlugin(DatabasePluginBase):
    plugin_name: str = "基础搜索"
    has_custom_widget: bool = True
    has_initialize: bool = True
    table_headers = BasicSearchDict
    table_show_headers: list[str] = [
        "商品名称",
        "品牌",
        "价格",
        "批次编号",
        "批次入库时间",
        "存库天数",
        "退货次数",
        "波次编号",
        "出库时间",
        "是否售出",
        "EAN13",
    ]

    def get_data(self) -> list[BasicSearchDict]:
        ean13 = self.custom_widget.get_ean13_le().text()
        name = self.custom_widget.get_name_le().text()
        brand = self.custom_widget.get_brand_le().text()
        price_enable = self.custom_widget.get_price_enable_sb().isChecked()
        price = self.custom_widget.get_price_sb().value()
        price_operation = self.custom_widget.get_price_operation_cb().currentIndex()
        price_operation = BasicSearchCombboxOperationEnum(price_operation)
        batch = self.custom_widget.get_batch_le().text()
        wave = self.custom_widget.get_wave_le().text()
        storage_days_enable = (
            self.custom_widget.get_storage_days_enable_sb().isChecked()
        )
        storage_days = self.custom_widget.get_storage_days_sb().value()
        storage_days_operation = (
            self.custom_widget.get_storage_days_operation_cb().currentIndex()
        )
        storage_days_operation = BasicSearchCombboxOperationEnum(storage_days_operation)
        hide_sold_item = self.custom_widget.get_hide_sold_item_cb().isChecked()
        hide_has_return_item = (
            self.custom_widget.get_hide_had_returns_item_cb().isChecked()
        )

        para: BasicSearchParameterDict = {
            "ean13": ean13,
            "name": name,
            "brand": brand,
            "has_price": price_enable,
            "price": price,
            "price_operation": price_operation,
            "batch_serial_number": batch,
            "wave_serial_number": wave,
            "has_storage_days": storage_days_enable,
            "storage_days": storage_days,
            "storage_days_operation": storage_days_operation,
            "hide_sold_item": hide_sold_item,
            "hide_has_return_item": hide_has_return_item,
        }

        return self._database_plugin_controller.get_basic_search_data(para)

    def get_description(self) -> str:
        return (
            "基础搜索,可以根据条件搜索商品\n"
            "所有的条件都是与的关系,如果你不希望某些选项被筛选请留空即可"
        )

    def get_custom_widget(self) -> QWidget:
        self.custom_widget = BasicSearchPluginComponentView()
        return self.custom_widget

    def _initialize(self) -> None:
        self.custom_widget = BasicSearchPluginComponentView()
        self._database_plugin_controller = DatabasePluginController()

    def _connect_signals(self) -> None: ...
