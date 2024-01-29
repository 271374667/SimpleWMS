from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QFrame, QWidget
from qfluentwidgets import (OptionsSettingCard, PushSettingCard, RangeSettingCard, SettingCardGroup)
from qfluentwidgets.components import ExpandLayout, LargeTitleLabel, SmoothScrollArea, ToolTipFilter

from src.config import cfg


# noinspection PyAttributeOutsideInit,PyTypeChecker
class SettingView(SmoothScrollArea):
    def __init__(self):
        super().__init__()
        self.scroll_widget = QWidget()
        self.expand_layout = ExpandLayout()

        self.setting_title = LargeTitleLabel("设置", self)

        self.create_card_group()
        self.create_card()
        self.set_up_tooltip()
        self.set_up_layout()
        self.initialize()

    def create_card_group(self) -> None:
        """创建卡片组"""
        self.general_group = SettingCardGroup("通用", self.scroll_widget)
        self.appearance_group = SettingCardGroup("外观", self.scroll_widget)
        self.storage_group = SettingCardGroup("存储", self.scroll_widget)

    def create_card(self) -> None:
        """创建卡片"""
        self.log_rotation_days_card = RangeSettingCard(cfg.log_rotation_days, QIcon(":/icons/images/icons/log.svg"),
                                                       "日志归档天数", "请选择多少天进行一次日志归档(将log打包为zip)",
                                                       self.general_group)
        self.log_retention_days_card = RangeSettingCard(cfg.log_retention_days,
                                                        QIcon(":/icons/images/icons/log.svg"),
                                                        "日志保留天数", "请选择日志最多保留多少天",
                                                        self.general_group)
        self.font_card = OptionsSettingCard(cfg.font, QIcon(":/icons/images/icons/choose_font.svg"), "字体",
                                            "请选择打印机字体粗细", [
                                                    '细', '常规', '中等', '粗', '加粗'
                                                    ], self.appearance_group)
        self.backup_path_card = PushSettingCard("备份路径", QIcon(":/icons/images/icons/save_archive.svg"),
                                                "请选择一个地址来进行备份", cfg.get(cfg.backup_path),
                                                self.storage_group)
        self.storage_path_card = PushSettingCard("入库文件保存路径", QIcon(":/icons/images/icons/save.svg"),
                                                 "请选择一个文件夹来保存入库的excel文件", cfg.get(cfg.storage_path),
                                                 self.storage_group)

        self.retrieval_path_card = PushSettingCard("出库文件保存路径", QIcon(":/icons/images/icons/save.svg"),
                                                   "请选择一个文件夹来保存出库的excel文件", cfg.get(cfg.retrieval_path),
                                                   self.storage_group)

    def set_up_tooltip(self) -> None:
        """设置卡片的提示"""
        self.log_rotation_days_card.setToolTip("日志归档天数越小,日志文件越多,但是每个日志文件的大小越小,默认为7天")
        self.log_retention_days_card.setToolTip("会删除过了指定时间的日志,默认为30天")
        self.font_card.setToolTip("字体越粗,打印机打印的字体越粗,默认为常规")
        self.storage_path_card.setToolTip("入库excel文件保存路径,默认为storage文件夹,文件夹下请不要存放其他文件")
        self.retrieval_path_card.setToolTip("出库excel文件保存路径,默认为retrieve文件夹,文件夹下请不要存放其他文件")

    def set_up_layout(self) -> None:
        """设置布局"""
        self.expand_layout.addWidget(self.general_group)
        self.expand_layout.addWidget(self.appearance_group)
        self.expand_layout.addWidget(self.storage_group)
        self.scroll_widget.setLayout(self.expand_layout)
        self.expand_layout.setSpacing(28)
        self.expand_layout.setContentsMargins(60, 10, 60, 0)

        # 给卡片组添加卡片
        self.general_group.addSettingCards(
                [self.log_rotation_days_card,
                        self.log_retention_days_card,
                        ])

        self.appearance_group.addSettingCards([self.font_card])
        self.storage_group.addSettingCards([self.backup_path_card, self.storage_path_card, self.retrieval_path_card])

        self.setWidget(self.scroll_widget)

    def initialize(self) -> None:
        """初始化窗体"""
        self.setWindowTitle("设置")
        self.setObjectName("setting_view")
        self.resize(1100, 800)
        self.setWidgetResizable(True)
        self.setFrameShape(QFrame.Shape.NoFrame)
        self.setting_title.move(60, 65)
        self.setViewportMargins(0, 120, 0, 20)

        for each in self.findChildren(QWidget):
            each.installEventFilter(ToolTipFilter(each, 200))


if __name__ == "__main__":
    import resource_rc as rc

    temp = rc.qt_resource_name  # 这里是为了不让pycharm格式化的时候把这个import删掉

    app = QApplication([])
    retrieval_view = SettingView()
    retrieval_view.show()
    app.exec()
