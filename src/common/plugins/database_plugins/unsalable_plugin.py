from PySide6.QtWidgets import QGroupBox, QHBoxLayout, QVBoxLayout, QWidget
from qfluentwidgets import BodyLabel, SpinBox, ToolTipFilter

from src.common.database.controller.database_plugin_controller import (
    DatabasePluginController,
)
from src.common.plugins.plugin_base import DatabasePluginBase
from src.dict_typing import UnsalableDict


class UnsalableWidget(QWidget):
    def __init__(self):
        super().__init__()

        # self.main_layout = FlowLayout(needAni=True, parent=self, isTight=True)
        self.main_layout = QVBoxLayout()

        # 设置第一阶段
        self.first_stage_group = QGroupBox("第一阶段")
        self.first_stage_layout = QHBoxLayout()
        self.first_stage_day_label = BodyLabel()
        self.first_stage_day_spin_box = SpinBox()
        self.first_state_value_label = BodyLabel()
        self.first_state_value_spin_box = SpinBox()

        # 设置第一阶段的文本框和标签
        self.first_stage_day_label.setText("轻微滞销天数:")
        self.first_stage_day_spin_box.setValue(3)
        self.first_stage_day_spin_box.setRange(0, 100)
        self.first_stage_day_spin_box.setSuffix("天")
        self.first_stage_day_spin_box.setSingleStep(1)
        self.first_stage_day_spin_box.setToolTip(
            "当商品存放时间在当前时间和中度滞销时间期间且满足轻微滞销的百分比,商品会被标记为滞销"
        )
        self.first_stage_day_label.setBuddy(self.first_stage_day_spin_box)
        self.first_stage_layout.addWidget(self.first_stage_day_label)
        self.first_stage_layout.addWidget(self.first_stage_day_spin_box)

        self.first_state_value_label.setText("轻微滞销百分比:")
        self.first_state_value_spin_box.setValue(80)
        self.first_state_value_spin_box.setRange(0, 100)
        self.first_state_value_spin_box.setSuffix("%")
        self.first_state_value_spin_box.setSingleStep(1)
        self.first_state_value_spin_box.setToolTip(
            "轻微滞销天数和中度滞销天数期间达到百分比数量的商品,会被标记为轻微滞销"
        )
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
        self.second_stage_day_label.setText("中等滞销天数:")
        self.second_stage_day_spin_box.setValue(7)
        self.second_stage_day_spin_box.setRange(1, 100)
        self.second_stage_day_spin_box.setSuffix("天")
        self.second_stage_day_spin_box.setSingleStep(1)
        self.second_stage_day_spin_box.setToolTip(
            "设置中等滞销的天数,该天数必须大于轻微滞销的天数,且小于严重滞销的天数"
        )
        self.second_stage_day_label.setBuddy(self.second_stage_day_spin_box)
        self.second_stage_layout.addWidget(self.second_stage_day_label)
        self.second_stage_layout.addWidget(self.second_stage_day_spin_box)

        self.second_state_value_label.setText("中等滞销百分比:")
        self.second_state_value_spin_box.setValue(70)
        self.second_state_value_spin_box.setRange(0, 100)
        self.second_state_value_spin_box.setSuffix("%")
        self.second_state_value_spin_box.setSingleStep(1)
        self.second_state_value_spin_box.setToolTip(
            "在中等滞销天数和严重滞销期间达到此百分比数量的商品,会被标记为中等滞销"
        )
        self.second_state_value_label.setBuddy(self.second_state_value_spin_box)
        self.second_stage_layout.addWidget(self.second_state_value_label)
        self.second_stage_layout.addWidget(self.second_state_value_spin_box)

        self.second_stage_group.setLayout(self.second_stage_layout)
        self.main_layout.addWidget(self.second_stage_group)

        # 设置第三阶段
        self.third_stage_group = QGroupBox("第三阶段")
        self.third_stage_layout = QHBoxLayout()
        self.third_stage_day_label = BodyLabel()
        self.third_stage_day_spin_box = SpinBox()

        # 设置第三阶段的文本框和标签
        self.third_stage_day_label.setText("严重滞销天数:")
        self.third_stage_day_spin_box.setValue(30)
        self.third_stage_day_spin_box.setRange(1, 100)
        self.third_stage_day_spin_box.setSuffix("天")
        self.third_stage_day_spin_box.setSingleStep(1)
        self.third_stage_day_spin_box.setToolTip(
            "设置严重滞销的天数,大于这个天数的商品都会被标记为严重滞销"
        )
        self.third_stage_day_label.setBuddy(self.third_stage_day_spin_box)
        self.third_stage_layout.addWidget(self.third_stage_day_label)
        self.third_stage_layout.addWidget(self.third_stage_day_spin_box)

        self.third_stage_group.setLayout(self.third_stage_layout)
        self.main_layout.addWidget(self.third_stage_group)

        # 设置一些规则
        self.first_state_value_spin_box.valueChanged.connect(self._validate_rule)
        self.second_state_value_spin_box.valueChanged.connect(self._validate_rule)
        self.first_stage_day_spin_box.valueChanged.connect(self._validate_rule)
        self.second_stage_day_spin_box.valueChanged.connect(self._validate_rule)
        self.third_stage_day_spin_box.valueChanged.connect(self._validate_rule)

        self.setLayout(self.main_layout)

        # self.setStyleSheet('background-color: #fcfcfc')
        for each in self.findChildren(QWidget):
            each.installEventFilter(ToolTipFilter(each, 200))

    def _validate_rule(self):
        # 首先是两个天数,中等滞销的天数必须大于轻微滞销的天数,严重滞销的天数必须大于中等滞销的天数
        if (
            self.first_stage_day_spin_box.value()
            >= self.second_stage_day_spin_box.value()
        ):
            self.second_stage_day_spin_box.setValue(
                self.first_stage_day_spin_box.value() + 1
            )
        if (
            self.second_stage_day_spin_box.value()
            >= self.third_stage_day_spin_box.value()
        ):
            self.third_stage_day_spin_box.setValue(
                self.second_stage_day_spin_box.value() + 1
            )
        # 然后是严重滞销的百分比必须小于中等滞销的百分比,中等滞销的百分比必须小于轻微滞销的百分比
        if (
            self.first_state_value_spin_box.value()
            <= self.second_state_value_spin_box.value()
        ):
            self.second_state_value_spin_box.setValue(
                self.first_state_value_spin_box.value() - 1
            )


class UnsalablePlugin(DatabasePluginBase):
    """
    滞销售商品插件

    滞销分为3个阶段，第一个阶段如果大于等于3天内小于7条库存量大于50%，那么就会被标记为轻微滞销
    第二个阶段如果大于7天，库存量还剩70%的商品，那么就会被标记为中等滞销
    第三个阶段如果30天内没有卖出的商品，全部会被标记为严重滞销

    上面的这些数据都需要可以直接在界面上设置
    """

    plugin_name: str = "滞销商品"
    table_show_headers = [
        "商品名称",
        "品牌",
        "批次",
        "存放天数",
        "库存量",
        "总量",
        "存货率%",
    ]
    table_headers = UnsalableDict
    has_custom_widget: bool = True
    has_initialize: bool = True

    def get_data(self) -> list[UnsalableDict]:
        unsalable_data = self._database_plugin_controller.get_unsalable_data()
        level_1_day = self._custom_widget.first_stage_day_spin_box.value()
        level_1_value = self._custom_widget.first_state_value_spin_box.value()
        level_2_day = self._custom_widget.second_stage_day_spin_box.value()
        level_2_value = self._custom_widget.second_state_value_spin_box.value()
        level_3_day = self._custom_widget.third_stage_day_spin_box.value()

        # 这里是对数据进行筛选
        result = []
        # each = (物品名称, 品牌, 批次, 在仓库中停留的天数, 存货数量, 总共进货, 存货率)
        for each in unsalable_data:
            level_1_condition = (
                (each["storage_time_from_today"] >= level_1_day)
                and (each["storage_time_from_today"] < level_2_day)
                and (each["storage_rate"] >= level_1_value)
            )
            level_2_condition = (each["storage_time_from_today"] >= level_2_day) and (
                each["storage_rate"] >= level_2_value
            )
            level_3_condition = each["storage_time_from_today"] >= level_3_day
            if level_1_condition or level_2_condition or level_3_condition:
                result.append(each)
        return result

    get_data.__doc__ = DatabasePluginBase.get_data.__doc__

    def get_description(self) -> str:
        return (
            "该插件用于筛选滞销商品,逻辑为根据批次,品牌,商品名称进行分组筛选\n"
            "其中存货率为(库存量/总量)的百分比,存放天数为从入库开始到今天为止的天数"
        )

    get_description.__doc__ = DatabasePluginBase.get_description.__doc__

    def get_custom_widget(self) -> QWidget:
        self._custom_widget = UnsalableWidget()
        return self._custom_widget

    get_custom_widget.__doc__ = DatabasePluginBase.get_custom_widget.__doc__

    def _initialize(self) -> None:
        self._custom_widget = UnsalableWidget()
        self._database_plugin_controller = DatabasePluginController()

    def _connect_signals(self) -> None: ...


if __name__ == "__main__":
    from PySide6.QtWidgets import QApplication

    app = QApplication([])
    unsalable_plugin = UnsalablePlugin()
    window = unsalable_plugin.get_custom_widget()
    window.show()
    # print(DatabasePluginManager.get_all_plugins())
    print(unsalable_plugin.get_data())
    app.exec()
