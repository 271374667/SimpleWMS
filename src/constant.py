from pathlib import Path

# Path to the root of the project
ROOT_DIR = Path(__file__).parent.parent.resolve()

SRC_DIR = ROOT_DIR / "src"
BACKUP_DIR = ROOT_DIR / "backup"
LOG_DIR = ROOT_DIR / "log"
ASSETS_DIR = ROOT_DIR / "assets"
IMAGES_DIR = ASSETS_DIR / "images"
UI_DIR = ASSETS_DIR / "ui"
FONT_DIR = ASSETS_DIR / "fonts"
RETRIEVE_DIR = ROOT_DIR / "retrieve"
STORAGE_DIR = ROOT_DIR / "storage"

# FILE
DATABASE_FILE = ROOT_DIR / "database.db"
CONFIG_FILE = ROOT_DIR / "config.json"
LOG_FILE = LOG_DIR / "log.log"
QRC_FILE = ASSETS_DIR / "resource.qrc"
QRC_PY_FILE = ROOT_DIR / "resource_rc.py"

# FONT
BOLD_FONT = FONT_DIR / "Alibaba-PuHuiTi-Bold.ttf"
HEAVY_FONT = FONT_DIR / "Alibaba-PuHuiTi-Heavy.ttf"
LIGHT_FONT = FONT_DIR / "Alibaba-PuHuiTi-Light.ttf"
MEDIUM_FONT = FONT_DIR / "Alibaba-PuHuiTi-Medium.ttf"
REGULAR_FONT = FONT_DIR / "Alibaba-PuHuiTi-Regular.ttf"


# 创建文件夹
def create_dir():
    for dir_ in [BACKUP_DIR,
            LOG_DIR,
            RETRIEVE_DIR,
            STORAGE_DIR]:
        if not dir_.exists():
            dir_.mkdir(parents=True)


create_dir()
