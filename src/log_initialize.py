import datetime

import loguru

from src.config import cfg
from src.constant import LOG_FILE


class LogInitialize:

    def initialize(self):
        loguru.logger.add(
                LOG_FILE,
                level="DEBUG",
                rotation=datetime.timedelta(cfg.get(cfg.log_rotation_days)),
                retention=datetime.timedelta(cfg.get(cfg.log_retention_days)),
                compression="zip",
                enqueue=True,
                )
