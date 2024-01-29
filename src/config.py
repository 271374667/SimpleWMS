from enum import Enum

from qfluentwidgets import (ConfigItem, EnumSerializer, FolderValidator, OptionsConfigItem, OptionsValidator, QConfig,
                            RangeConfigItem, RangeValidator, qconfig)

from src.constant import (BACKUP_DIR, BOLD_FONT, CONFIG_FILE, HEAVY_FONT, LIGHT_FONT, MEDIUM_FONT, REGULAR_FONT,
                          RETRIEVE_DIR, STORAGE_DIR)


class Font(Enum):
    LIGHT = str(LIGHT_FONT)
    REGULAR = str(REGULAR_FONT)
    MEDIUM = str(MEDIUM_FONT)
    BOLD = str(BOLD_FONT)
    HEAVY = str(HEAVY_FONT)


class Config(QConfig):
    # General
    font = OptionsConfigItem("Appearance", "打印字体", Font.REGULAR, OptionsValidator(Font), EnumSerializer(Font))
    # Backup
    backup_path = ConfigItem("General", "备份路径", str(BACKUP_DIR), FolderValidator())
    log_rotation_days = RangeConfigItem("General", "日志归档天数", 7, RangeValidator(1, 30))
    log_retention_days = RangeConfigItem("General", "日志保留天数", 30, RangeValidator(1, 90))

    # 存储
    storage_path = ConfigItem("General", "入库文件保存路径", str(STORAGE_DIR), FolderValidator())
    retrieval_path = ConfigItem("General", "出库文件保存路径", str(RETRIEVE_DIR), FolderValidator())


cfg = Config()
cfg.file = CONFIG_FILE
qconfig.load(CONFIG_FILE, cfg)
