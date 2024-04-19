from PySide6.QtWidgets import QApplication, QWidget
from qfluentwidgets import ToolTipFilter
from qfluentwidgets.components import (
    CheckBox,
    ComboBox,
    DoubleSpinBox,
    LineEdit,
    PushButton,
    SpinBox,
    SwitchButton,
    )

from src.core.enums import BasicSearchCombboxOperationEnum
from src.core.wms_dataclass import BasicSearchDataclass
from src.interface.Ui_basic_search_plugin_component import Ui_Form


class BasicSearchPluginComponentView(QWidget):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        operation = ["等于", "大于", "小于"]

        # 将dataclasses添加到排序里面
        self.get_sort_column_cb().addItems(BasicSearchDataclass.__annotations__.keys())
        self.get_sort_order_cb().addItems(["升序", "降序"])

        for each in BasicSearchCombboxOperationEnum:
            self.get_price_operation_cb().addItem(operation[each.value])
            self.get_storage_days_operation_cb().addItem(operation[each.value])

        self.get_retype_btn().clicked.connect(self.retype_btn_clicked)

        for each in self.findChildren(QWidget):
            each.installEventFilter(ToolTipFilter(each, 200))

    def get_ean13_le(self) -> LineEdit:
        return self.ui.LineEdit_3

    def get_name_le(self) -> LineEdit:
        return self.ui.LineEdit_5

    def get_brand_le(self) -> LineEdit:
        return self.ui.LineEdit

    def get_price_operation_cb(self) -> ComboBox:
        return self.ui.ComboBox

    def get_price_sb(self) -> DoubleSpinBox:
        return self.ui.DoubleSpinBox

    def get_price_enable_sb(self) -> SwitchButton:
        return self.ui.SwitchButton

    def get_batch_le(self) -> LineEdit:
        return self.ui.LineEdit_2

    def get_wave_le(self) -> LineEdit:
        return self.ui.LineEdit_4

    def get_storage_days_operation_cb(self) -> ComboBox:
        return self.ui.ComboBox_2

    def get_storage_days_sb(self) -> SpinBox:
        return self.ui.SpinBox

    def get_storage_days_enable_sb(self) -> SwitchButton:
        return self.ui.SwitchButton_2

    def get_retype_btn(self) -> PushButton:
        return self.ui.PushButton

    def get_hide_sold_item_cb(self) -> CheckBox:
        return self.ui.CheckBox

    def get_hide_had_returns_item_cb(self) -> CheckBox:
        return self.ui.CheckBox_2

    def get_sort_column_cb(self) -> ComboBox:
        return self.ui.ComboBox_3

    def get_sort_order_cb(self) -> ComboBox:
        return self.ui.ComboBox_4

    def get_sort_enable_sb(self) -> SwitchButton:
        return self.ui.SwitchButton_4

    def retype_btn_clicked(self) -> None:
        self.get_price_sb().setValue(0)
        self.get_price_operation_cb().setCurrentIndex(0)
        self.get_storage_days_sb().setValue(0)
        self.get_storage_days_operation_cb().setCurrentIndex(0)
        self.get_price_enable_sb().setChecked(False)
        self.get_storage_days_enable_sb().setChecked(False)
        self.get_sort_column_cb().setCurrentIndex(0)
        self.get_sort_order_cb().setCurrentIndex(0)
        self.get_sort_enable_sb().setChecked(False)


if __name__ == "__main__":
    app = QApplication([])
    w = BasicSearchPluginComponentView()
    w.show()
    app.exec()
