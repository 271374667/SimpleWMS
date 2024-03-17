from PySide6.QtGui import QPainter, QPixmap
from PySide6.QtPrintSupport import QPrinter
from PySide6.QtWidgets import QApplication

from src.utils.singleton import Singleton


@Singleton
class Printer:
    def __init__(self):
        self.printer = QPrinter(QPrinter.HighResolution)
        self.printer.setPrinterName("NIIMBOT B3S")
        self.printer.setResolution(203)
        self.printer.setFullPage(False)
        self.printer.setCopyCount(1)
        self.painter = QPainter()
        self.painter.begin(self.printer)

    def print_image(self, pixmap: QPixmap):
        if not isinstance(pixmap, QPixmap):
            raise TypeError("The input must be QPixmap.")
        print(self.printer.isValid())
        if not self.printer.isValid():
            raise ValueError("failed to open file, is it writable?")

        print(self.printer.newPage())
        if not self.printer.newPage():
            raise RuntimeError("failed in flushing page to disk, disk full?")

        pixmap = pixmap.scaled(560, 300)
        self.painter.drawPixmap(0, 0, pixmap)
        self.painter.end()
        print("打印成功")


if __name__ == "__main__":
    app = QApplication([])
    printer = Printer()
    printer.print_image(QPixmap(r"E:\load\python\Project\SimpleWMS\PixPin.png"))
    app.exec()
