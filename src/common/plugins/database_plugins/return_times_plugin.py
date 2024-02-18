from datetime import datetime

from PySide6.QtCore import QDate
from PySide6.QtWidgets import QApplication, QHBoxLayout, QVBoxLayout, QWidget
from qfluentwidgets import ToolTipFilter
from qfluentwidgets.components import BodyLabel, CalendarPicker, PushButton

from src.common.database.controller.database_plugin_controller import DatabasePluginController
from src.common.plugins.plugin_base import DatabasePluginBase
from src.dict_typing import ReturnTimesDict


class CustomWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.main_layout = QVBoxLayout()

        # 设置起始时间
        self.start_layout = QHBoxLayout()
        self.start_lb = BodyLabel()
        self.start_lb.setText('设置起始时间:')
        self.start_calendar_picker = CalendarPicker()
        self.start_calendar_picker.setText('起始时间')
        self.start_calendar_picker.setDateFormat('yyyy-MM-dd')
        self.start_setting_btn = PushButton()
        self.start_setting_btn.setText('将起始时间设为2000年1月1日')
        self.start_setting_btn.setToolTip('使用这样的方式可以查看所有的退货率')

        self.start_layout.addWidget(self.start_lb)
        self.start_layout.addWidget(self.start_calendar_picker)
        self.start_layout.addWidget(self.start_setting_btn)
        self.main_layout.addLayout(self.start_layout)

        # 设置结束时间
        self.end_layout = QHBoxLayout()
        self.end_lb = BodyLabel()
        self.end_lb.setText('设置结束时间:')
        self.end_calendar_picker = CalendarPicker()
        self.end_calendar_picker.setText('结束时间')
        self.end_calendar_picker.setDateFormat('yyyy-MM-dd')
        self.end_calendar_btn = PushButton()
        self.end_calendar_btn.setText('将所有时间设为今天')
        self.end_calendar_btn.setToolTip('使用这样的方式可以查看到今天的退货率')

        self.end_layout.addWidget(self.end_lb)
        self.end_layout.addWidget(self.end_calendar_picker)
        self.end_layout.addWidget(self.end_calendar_btn)
        self.main_layout.addLayout(self.end_layout)

        self.setLayout(self.main_layout)

        self.start_setting_btn.clicked.connect(self.set_start_time_from_2000)
        self.end_calendar_btn.clicked.connect(self.set_end_time_today)

        for each in self.findChildren(QWidget):
            each.installEventFilter(ToolTipFilter(each, 200))

    def set_start_time_from_2000(self):
        self.start_calendar_picker.setDate(QDate(2000, 1, 1))

    def set_end_time_today(self):
        today = datetime.today()
        self.end_calendar_picker.setDate(QDate(today.year, today.month, today.day))
        self.start_calendar_picker.setDate(QDate(today.year, today.month, today.day))


class ReturnTimesPlugin(DatabasePluginBase):
    plugin_name: str = '查看退货率'
    has_custom_widget: bool = True
    has_initialize: bool = True
    table_show_headers: list[str] = ['商品名称', '品牌', '批次号', '入库时间', '退货次数', 'EAN13']
    table_headers = ReturnTimesDict

    def get_data(self) -> list[ReturnTimesDict]:
        data = self._database_plugin_controller.get_return_data()
        # 根据时间进行筛选
        start_time = self._custom_widget.start_calendar_picker.getDate()
        end_time = self._custom_widget.end_calendar_picker.getDate()

        if not start_time.isValid() or not end_time.isValid():
            return data

        start_time = self._custom_widget.start_calendar_picker.date.toPython()
        end_time = self._custom_widget.end_calendar_picker.date.toPython()

        if start_time >= end_time:
            start_time, end_time = end_time, start_time

        data = [i for i in data if (start_time <= i['storage_time'].date()) and (i['storage_time'].date() <= end_time)]
        return data

    def get_description(self) -> str:
        return ('查看退货情况, 可以通过点击表头进行排序\n'
                '默认情况下直接点击开始查找按钮即可查看所有的退货情况')

    def get_custom_widget(self) -> QWidget:
        self._custom_widget = CustomWidget()
        return self._custom_widget

    def _initialize(self) -> None:
        self._custom_widget = CustomWidget()
        self._database_plugin_controller = DatabasePluginController()

    def _connect_signals(self) -> None:
        pass


if __name__ == '__main__':
    app = QApplication([])
    widget = CustomWidget()
    widget.show()
    app.exec()
