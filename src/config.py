from enum import Enum

from qfluentwidgets import (
    ConfigItem,
    EnumSerializer,
    FolderValidator,
    OptionsConfigItem,
    OptionsValidator,
    QConfig,
    RangeConfigItem,
    RangeValidator,
    qconfig,
)

from src.core.constant import (
    BACKUP_DIR,
    BOLD_FONT,
    CONFIG_FILE,
    HEAVY_FONT,
    LIGHT_FONT,
    MEDIUM_FONT,
    REGULAR_FONT,
    RETRIEVE_DIR,
    STORAGE_DIR,
)

__version__ = "0.0.8"


class Font(Enum):
    LIGHT = str(LIGHT_FONT)
    REGULAR = str(REGULAR_FONT)
    MEDIUM = str(MEDIUM_FONT)
    BOLD = str(BOLD_FONT)
    HEAVY = str(HEAVY_FONT)


class Config(QConfig):
    # General
    email_account = ConfigItem("General", "邮箱", "", None)
    email_secret_key = ConfigItem("General", "密码", "", None)

    # 日志
    log_rotation_days = RangeConfigItem(
        "General", "日志归档天数", 7, RangeValidator(1, 30)
    )
    log_retention_days = RangeConfigItem(
        "General", "日志保留天数", 30, RangeValidator(1, 90)
    )

    # 存储
    backup_path = ConfigItem("Storage", "备份路径", str(BACKUP_DIR), FolderValidator())
    storage_path = ConfigItem(
        "Storage", "入库文件保存路径", str(STORAGE_DIR), FolderValidator()
    )
    retrieval_path = ConfigItem(
        "Storage", "出库文件保存路径", str(RETRIEVE_DIR), FolderValidator()
    )

    # 外观
    font = OptionsConfigItem(
        "Appearance",
        "打印字体",
        Font.REGULAR,
        OptionsValidator(Font),
        EnumSerializer(Font),
    )


cfg = Config()
cfg.file = CONFIG_FILE
if not CONFIG_FILE.exists():
    cfg.save()
qconfig.load(CONFIG_FILE, cfg)
