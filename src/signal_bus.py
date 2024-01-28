from PySide6.QtCore import QObject, Signal

from src.utils.singleton import Singleton


@Singleton
class SingnalBus(QObject):
    lazer_gun_message = Signal(str)
