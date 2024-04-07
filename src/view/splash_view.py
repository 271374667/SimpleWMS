from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QPixmap
from PySide6.QtWidgets import QApplication, QSplashScreen

from src.core.constant import SPLASH_IMAGE_PATH
from src.utils.singleton import Singleton


@Singleton
class SplashView(QSplashScreen):
    def __init__(self):
        super().__init__()
        self.setPixmap(QPixmap(str(SPLASH_IMAGE_PATH)))
        QApplication.instance().processEvents()

        # 窗口最顶层
        self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint | Qt.FramelessWindowHint)

    def mousePressEvent(self, event):
        pass

    def show_message(self, message: str):
        self.showMessage(
            message,
            alignment=Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignCenter,
            color=QColor(173, 216, 255),
        )
        QApplication.instance().processEvents()


if __name__ == "__main__":
    import time

    app = QApplication([])
    splash_view = SplashView()
    splash_view.show()
    splash_view.show_message("正在加载程序...")
    time.sleep(2)
    splash_view.show_message("加载完成...")

    app.exec()
