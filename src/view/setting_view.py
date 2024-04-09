from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QFrame, QVBoxLayout, QWidget
from qfluentwidgets import (
    FluentIcon,
    Icon,
    OptionsSettingCard,
    PrimaryPushSettingCard,
    ProgressBar,
    PushSettingCard,
    RangeSettingCard,
    SettingCardGroup,
    )
from qfluentwidgets.components import (
    ExpandLayout,
    LargeTitleLabel,
    SmoothScrollArea,
    ToolTipFilter,
    )

from src.config import cfg
from src.view.message_base_view import MessageBaseView


class SettingView(MessageBaseView):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.main_layout = QVBoxLayout()
        self.smooth_scroll_area = SmoothScrollArea()

        # 这里是一个补丁,因为不知道为什么MessageBaseView没有调用父类的构造函数
        # 所以这里手动初始化一下
        self.is_state_tooltip_running: bool = False

        self.scroll_widget = QWidget()
        self.expand_layout = ExpandLayout(self.scroll_widget)

        self.setting_title = LargeTitleLabel()
        self.setting_title.setText("设置")

        self.progress_bar = ProgressBar()
        self.progress_bar.setTextVisible(True)

        self._create_card_group()
        self._create_card()
        self._set_up_tooltip()
        self._set_up_layout()
        self._initialize()

    def get_progress_bar(self) -> ProgressBar:
        return self.progress_bar

    def scroll_to_general_group(self) -> None:
        """滚动到一般的卡片组"""
        self.smooth_scroll_area.verticalScrollBar().setValue(self.general_group.y())

    def scroll_to_appearance_group(self) -> None:
        """滚动到外观的卡片组"""
        self.smooth_scroll_area.verticalScrollBar().setValue(self.appearance_group.y())

    def scroll_to_storage_group(self) -> None:
        """滚动到存储的卡片组"""
        self.smooth_scroll_area.verticalScrollBar().setValue(self.storage_group.y())

    def _create_card_group(self) -> None:
        """创建卡片组"""
        self.general_group = SettingCardGroup("通用", self.scroll_widget)
        self.appearance_group = SettingCardGroup("外观", self.scroll_widget)
        self.storage_group = SettingCardGroup("存储", self.scroll_widget)

    def _create_card(self) -> None:
        """创建卡片"""
        self.log_rotation_days_card = RangeSettingCard(
            cfg.log_rotation_days,
            QIcon(":/icons/images/icons/log.svg"),
            "日志归档天数",
            "请选择多少天进行一次日志归档(将log打包为zip)",
            self.general_group,
        )
        self.log_retention_days_card = RangeSettingCard(
            cfg.log_retention_days,
            QIcon(":/icons/images/icons/log.svg"),
            "日志保留天数",
            "请选择日志最多保留多少天",
            self.general_group,
        )
        self.font_card = OptionsSettingCard(
            cfg.font,
            QIcon(":/icons/images/icons/choose_font.svg"),
            "字体",
            "请选择打印机字体粗细",
            ["细", "常规", "中等", "粗", "加粗"],
            self.appearance_group,
        )
        self.backup_path_card = PushSettingCard(
            "备份路径",
            QIcon(":/icons/images/icons/save_archive.svg"),
            "请选择一个地址来进行备份",
            cfg.get(cfg.backup_path),
            self.storage_group,
        )
        self.storage_path_card = PushSettingCard(
            "入库文件保存路径",
            QIcon(":/icons/images/icons/save.svg"),
            "请选择一个文件夹来保存入库的excel文件",
            cfg.get(cfg.storage_path),
            self.storage_group,
        )

        self.retrieval_path_card = PushSettingCard(
            "出库文件保存路径",
            QIcon(":/icons/images/icons/save.svg"),
            "请选择一个文件夹来保存出库的excel文件",
            cfg.get(cfg.retrieval_path),
            self.storage_group,
        )

        self.email_account_card = PrimaryPushSettingCard(
            "邮箱设置",
            QIcon(":/icons/images/icons/email.svg"),
            "设置您的邮箱",
            "设置您的邮箱账号和密钥,用于发送邮件,如果您不需要发送邮件,可以不设置",
            self.general_group,
        )

        self.export_database_card = PushSettingCard(
            "导出数据库",
            Icon(FluentIcon.EMBED),
            "导出数据库",
            "导出数据库为xlsx文件,请注意导出的文件可能会很大,请耐心等待",
            self.storage_group,
        )

        self.import_database_card = PushSettingCard(
            "导入数据库",
            Icon(FluentIcon.DOWNLOAD),
            "导入数据库",
            "导入数据库,请注意导入数据库之前需要先确保自己的数据库是空的",
            self.storage_group,
        )

        self.max_table_rows_card = RangeSettingCard(
            cfg.max_table_rows,
            Icon(FluentIcon.UNIT),
            "表格最大行数",
            "设置表格最大行数,默认为50",
            self.general_group,
        )

    def _set_up_tooltip(self) -> None:
        """设置卡片的提示"""
        self.log_rotation_days_card.setToolTip(
            "日志归档天数越小,日志文件越多,但是每个日志文件的大小越小,默认为7天"
        )
        self.log_retention_days_card.setToolTip("会删除过了指定时间的日志,默认为30天")
        self.font_card.setToolTip("字体越粗,打印机打印的字体越粗,默认为常规")
        self.storage_path_card.setToolTip(
            "入库excel文件保存路径,默认为storage文件夹,文件夹下请不要存放其他文件"
        )
        self.retrieval_path_card.setToolTip(
            "出库excel文件保存路径,默认为retrieve文件夹,文件夹下请不要存放其他文件"
        )
        self.email_account_card.setToolTip(
            "您需要设置您邮箱的账号和密钥(注意这里密钥不等于密码)"
        )
        self.export_database_card.setToolTip(
            "导出数据库为xlsx文件,请注意导出之后不要修改文件内容,否则无法导入"
        )
        self.import_database_card.setToolTip(
            "导入指定的xlsx文件,请注意只能导入由本软件导出的xlsx文件,否则无法导入"
        )

        self.max_table_rows_card.setToolTip(
            "设置表格最大行数,显示的行数越多,占用的内存越大,默认为50行"
        )

    def _set_up_layout(self) -> None:
        """设置布局"""
        self.smooth_scroll_area.setWidget(self.scroll_widget)

        self.expand_layout.addWidget(self.general_group)
        self.expand_layout.addWidget(self.appearance_group)
        self.expand_layout.addWidget(self.storage_group)
        self.scroll_widget.setLayout(self.expand_layout)
        self.expand_layout.setSpacing(28)
        self.expand_layout.setContentsMargins(60, 10, 60, 0)

        # 给卡片组添加卡片
        self.general_group.addSettingCard(self.email_account_card)
        self.general_group.addSettingCard(self.log_rotation_days_card)
        self.general_group.addSettingCard(self.log_retention_days_card)
        self.general_group.addSettingCard(self.max_table_rows_card)

        self.appearance_group.addSettingCard(self.font_card)

        self.storage_group.addSettingCard(self.backup_path_card)
        self.storage_group.addSettingCard(self.storage_path_card)
        self.storage_group.addSettingCard(self.retrieval_path_card)
        self.storage_group.addSettingCard(self.export_database_card)
        self.storage_group.addSettingCard(self.progress_bar)
        self.storage_group.addSettingCard(self.import_database_card)

    def _initialize(self) -> None:
        """初始化窗体"""
        self.setWindowTitle("设置")
        self.setObjectName("setting_view")
        self.resize(1100, 800)
        self.smooth_scroll_area.setWidgetResizable(True)
        self.smooth_scroll_area.setFrameShape(QFrame.Shape.NoFrame)
        # self.setting_title.move(60, 65)
        self.setting_title.setMargin(30)
        self.setting_title.setFixedWidth(200)
        # self.smooth_scroll_area.setViewportMargins(0, 120, 0, 0)

        self.main_layout.addWidget(self.setting_title)
        self.main_layout.addWidget(self.smooth_scroll_area)
        self.setLayout(self.main_layout)

        # 这里因为背景色不一样,我手动打个补丁
        self.setStyleSheet("background-color: #fcfcfc")
        self.smooth_scroll_area.setStyleSheet("background-color: #fcfcfc")
        # self.setting_title.setStyleSheet('background-color: #fcfcfc')

        for each in self.findChildren(QWidget):
            each.installEventFilter(ToolTipFilter(each, 200))


if __name__ == "__main__":
    import resource_rc as rc

    temp = rc.qt_resource_name  # 这里是为了不让pycharm格式化的时候把这个import删掉

    app = QApplication([])
    retrieval_view = SettingView()
    retrieval_view.show()
    retrieval_view.scroll_to_storage_group()
    app.exec()
