from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QFrame, QWidget
from qfluentwidgets import (OptionsSettingCard, PushSettingCard, RangeSettingCard, SettingCardGroup)
from qfluentwidgets.components import ExpandLayout, SmoothScrollArea, ToolTipFilter

from src.config import cfg


class SettingView(SmoothScrollArea):
    def __init__(self):
        super().__init__()
        self.scroll_widget = QWidget()
        self.expand_layout = ExpandLayout()

        # 通用设置
        self.general_group = SettingCardGroup("通用", self.scroll_widget)
        self.backup_path_card = PushSettingCard("备份路径", QIcon(":/icons/images/icons/save_archive.svg"),
                                                "请选择一个地址来进行备份", cfg.get(cfg.backup_path),
                                                self.general_group)

        self.log_rotation_days_card = RangeSettingCard(cfg.log_rotation_days, QIcon(":/icons/images/icons/log.svg"),
                                                       "日志归档天数", "请选择多少天进行一次日志归档(将log打包为zip)",
                                                       self.general_group)
        self.log_rotation_days_card.setToolTip("日志归档天数越小,日志文件越多,但是每个日志文件的大小越小,默认为7天")

        self.log_retention_days_card = RangeSettingCard(cfg.log_retention_days,
                                                        QIcon(":/icons/images/icons/log.svg"),
                                                        "日志保留天数", "请选择日志最多保留多少天",
                                                        self.general_group)
        self.log_retention_days_card.setToolTip("会删除过了指定时间的日志,默认为30天")

        # 外观设置
        self.appearance_group = SettingCardGroup("外观", self.scroll_widget)
        self.font_card = OptionsSettingCard(cfg.font, QIcon(":/icons/images/icons/choose_font.svg"), "字体",
                                            "请选择打印机字体粗细", [
                                                    '细', '常规', '中等', '粗', '加粗'
                                                    ], self.appearance_group)
        self.font_card.setToolTip("字体越粗,打印机打印的字体越粗,默认为常规")

        # 预警系统设置
        self.warning_group = SettingCardGroup("预警", self.scroll_widget)

        self.initialize()

    def initialize(self) -> None:
        self.setWindowTitle("设置")
        self.setObjectName("setting_view")
        self.resize(1100, 800)
        self.setWidgetResizable(True)
        self.setFrameShape(QFrame.NoFrame)
        self.general_group.addSettingCards(
                [self.backup_path_card, self.log_rotation_days_card, self.log_retention_days_card])
        self.appearance_group.addSettingCards([self.font_card])
        self.expand_layout.addWidget(self.general_group)
        self.expand_layout.addWidget(self.appearance_group)
        self.scroll_widget.setLayout(self.expand_layout)
        self.setWidget(self.scroll_widget)
        self.expand_layout.setSpacing(28)
        self.expand_layout.setContentsMargins(60, 10, 60, 0)

        for each in self.findChildren(QWidget):
            each.installEventFilter(ToolTipFilter(each, 200))


if __name__ == "__main__":
    import resource_rc

    app = QApplication([])
    retrieval_view = SettingView()
    retrieval_view.show()
    app.exec()
