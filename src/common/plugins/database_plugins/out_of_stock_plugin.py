from PySide6.QtWidgets import QGroupBox, QHBoxLayout, QVBoxLayout, QWidget
from qfluentwidgets import BodyLabel, SpinBox, ToolTipFilter

from src.common.database.controller.database_plugin_controller import (
    DatabasePluginController,
)
from src.common.plugins.plugin_base import DatabasePluginBase
from src.core.dict_typing import OutOfStockDict
from src.core.wms_dataclass import OutOfStockDataclass


class OutOfStockWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.main_layout = QVBoxLayout()

        # 设置第一阶段
        self.first_stage_group = QGroupBox("第一阶段")
        self.first_stage_layout = QHBoxLayout()
        self.first_stage_day_label = BodyLabel()
        self.first_stage_day_spin_box = SpinBox()
        self.first_state_value_label = BodyLabel()
        self.first_state_value_spin_box = SpinBox()

        # 设置第一阶段的文本框和标签
        self.first_stage_day_label.setText("轻微脱销天数:")
        self.first_stage_day_spin_box.setValue(3)
        self.first_stage_day_spin_box.setRange(0, 100)
        self.first_stage_day_spin_box.setSuffix("天")
        self.first_stage_day_spin_box.setSingleStep(1)
        self.first_stage_day_spin_box.setToolTip(
            "该天数不能大于中等滞销的天数\n该天数内存货率小于百分比会被标记为脱销"
        )
        self.first_stage_day_label.setBuddy(self.first_stage_day_spin_box)
        self.first_stage_layout.addWidget(self.first_stage_day_label)
        self.first_stage_layout.addWidget(self.first_stage_day_spin_box)

        self.first_state_value_label.setText("轻微脱销百分比:")
        self.first_state_value_spin_box.setValue(50)
        self.first_state_value_spin_box.setRange(0, 100)
        self.first_state_value_spin_box.setSuffix("%")
        self.first_state_value_spin_box.setSingleStep(1)
        self.first_state_value_spin_box.setToolTip("当存货率小于该百分百则会被显示")
        self.first_state_value_label.setBuddy(self.first_state_value_spin_box)
        self.first_stage_layout.addWidget(self.first_state_value_label)
        self.first_stage_layout.addWidget(self.first_state_value_spin_box)

        self.first_stage_group.setLayout(self.first_stage_layout)
        self.main_layout.addWidget(self.first_stage_group)

        # 设置第二阶段
        self.second_stage_group = QGroupBox("第二阶段")
        self.second_stage_layout = QHBoxLayout()
        self.second_stage_day_label = BodyLabel()
        self.second_stage_day_spin_box = SpinBox()
        self.second_state_value_label = BodyLabel()
        self.second_state_value_spin_box = SpinBox()

        # 设置第二阶段的文本框和标签
        self.second_stage_day_label.setText("中等脱销天数:")
        self.second_stage_day_spin_box.setValue(7)
        self.second_stage_day_spin_box.setRange(1, 30)
        self.second_stage_day_spin_box.setSuffix("天")
        self.second_stage_day_spin_box.setSingleStep(1)
        self.second_stage_day_spin_box.setToolTip(
            "设置时需要注意,值不能大于轻微脱销的天数"
        )
        self.second_stage_day_label.setBuddy(self.second_stage_day_spin_box)
        self.second_stage_layout.addWidget(self.second_stage_day_label)
        self.second_stage_layout.addWidget(self.second_stage_day_spin_box)

        self.second_state_value_label.setText("中等脱销百分比:")
        self.second_state_value_spin_box.setValue(30)
        self.second_state_value_spin_box.setRange(0, 100)
        self.second_state_value_spin_box.setSuffix("%")
        self.second_state_value_spin_box.setSingleStep(1)
        self.second_state_value_spin_box.setToolTip("该数值不能大于轻微脱销的百分比")
        self.second_state_value_label.setBuddy(self.second_state_value_spin_box)
        self.second_stage_layout.addWidget(self.second_state_value_label)
        self.second_stage_layout.addWidget(self.second_state_value_spin_box)

        self.second_stage_group.setLayout(self.second_stage_layout)
        self.main_layout.addWidget(self.second_stage_group)

        # 设置一些规则
        self.first_state_value_spin_box.valueChanged.connect(self._validate_rule)
        self.second_state_value_spin_box.valueChanged.connect(self._validate_rule)
        self.first_stage_day_spin_box.valueChanged.connect(self._validate_rule)
        self.second_stage_day_spin_box.valueChanged.connect(self._validate_rule)

        self.setLayout(self.main_layout)

        for each in self.findChildren(QWidget):
            each.installEventFilter(ToolTipFilter(each, 200))

    def _validate_rule(self):
        # 首先是两个天数,中等脱销的天数必须大于轻微脱销的天数
        if (
            self.first_stage_day_spin_box.value()
            >= self.second_stage_day_spin_box.value()
        ):
            self.second_stage_day_spin_box.setValue(
                self.first_stage_day_spin_box.value() + 1
            )
        # 然后是中等脱销的百分比必须小于轻微脱销的百分比
        if (
            self.first_state_value_spin_box.value()
            <= self.second_state_value_spin_box.value()
        ):
            self.second_state_value_spin_box.setValue(
                self.first_state_value_spin_box.value() - 1
            )


class OutOfStockPlugin(DatabasePluginBase):
    """
    脱销商品插件,用于筛选滞销商品

    - 3天之内，库存小于等于50%
    - 7天之内，库存小于等于30%

    上面的这些数据都需要可以直接在界面上设置
    """

    plugin_name: str = "脱销商品"
    has_custom_widget: bool = True
    has_initialize: bool = True
    table_dataclass = OutOfStockDataclass

    def get_data(self) -> list[OutOfStockDataclass]:
        outofstock_data = self._database_plugin_controller.get_out_of_stock_data()
        level_1_day = self._custom_widget.first_stage_day_spin_box.value()
        level_1_value = self._custom_widget.first_state_value_spin_box.value()
        level_2_day = self._custom_widget.second_stage_day_spin_box.value()
        level_2_value = self._custom_widget.second_state_value_spin_box.value()

        # 这里是对数据进行筛选
        result: list[OutOfStockDataclass] = []

        for each in outofstock_data:
            level_1_condition = (each.入库天数 <= level_1_day) and (
                each.库存量 <= level_1_value
            )
            level_2_condition = (each.入库天数 <= level_2_day) and (
                each.存货率 <= level_2_value
            )
            if level_1_condition or level_2_condition:
                result.append(each)
        return result

    get_data.__doc__ = DatabasePluginBase.get_data.__doc__

    def get_description(self) -> str:
        return (
            "该插件用于筛选脱销商品,逻辑为根据批次,品牌,商品名称进行分组筛选\n"
            "其中存货率为(库存量/总量)的百分比,存放天数为从入库开始到今天为止的天数"
        )

    get_description.__doc__ = DatabasePluginBase.get_description.__doc__

    def get_custom_widget(self) -> QWidget:
        self._custom_widget = OutOfStockWidget()
        return self._custom_widget

    get_custom_widget.__doc__ = DatabasePluginBase.get_custom_widget.__doc__

    def _initialize(self) -> None:
        self._custom_widget = OutOfStockWidget()
        self._database_plugin_controller = DatabasePluginController()

    def _connect_signals(self) -> None: ...


if __name__ == "__main__":
    from PySide6.QtWidgets import QApplication

    app = QApplication([])
    unsalable_plugin = OutOfStockPlugin()
    window = unsalable_plugin.get_custom_widget()
    window.show()
    # print(DatabasePluginManager.get_all_plugins())
    print(unsalable_plugin.get_data())
    app.exec()
