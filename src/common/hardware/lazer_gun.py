"""
扫码枪对接模块

使用方法如下:
1. 在需要使用扫码枪的地方导入LazerGun类
2. 在需要使用扫码枪的地方实例化LazerGun类
3. 在需要使用扫码枪的地方调用LazerGun类的start方法
4. 在需要使用扫码枪的地方连接信号bus的lazer_gun_message信号,并且将槽函数设置为接收扫码枪的消息

注意:
    由于扫码枪的输入是监听全体键盘输入,所以在使用扫码枪的地方,不要使用键盘输入
"""

import loguru
from PySide6.QtCore import QObject, Signal
from PySide6.QtWidgets import QApplication
from pynput import keyboard

from src.utils.run_in_thread import RunInThread
from src.utils.singleton import Singleton
from src.signal_bus import SingnalBus


@Singleton
class ClipBoard(QObject):
    message = Signal(str)

    def __init__(self):
        super().__init__()
        self.ean13_input: str = ''

    def on_release(self, key):
        try:
            self.ean13_input += key.char
        except Exception:
            try:
                if key == key.enter:  # 如果扫码枪中的数据是回车enter按键
                    if len(self.ean13_input) != 13 or self.ean13_input.isdigit() is False:
                        loguru.logger.debug(f'当前输入的条形码格式错误,重新扫描')
                        self.ean13_input = ''
                        return
                    loguru.logger.debug(f'当前输入的条形码为{self.ean13_input}')
                    self.message.emit(self.ean13_input)
                    self.ean13_input = ''
            except Exception as e:
                self.ean13_input = ''
                loguru.logger.critical(e)

    def start_listen(self):
        # 监听键盘扫码枪输入
        with keyboard.Listener(on_release=self.on_release) as listener:
            listener.join()


@Singleton
class LazerGun(QObject):
    def __init__(self):
        super().__init__()
        self.run_in_thread = RunInThread()
        self.clip_board = ClipBoard()

    def start(self):
        self.run_in_thread.set_start_func(self.clip_board.start_listen)
        self.run_in_thread.start()
        loguru.logger.info('扫码枪监听线程启动……')

    def _send2signal_bus(self, message: str):
        SingnalBus().lazer_gun_message.emit(message)


if __name__ == "__main__":
    def show_message(message: list[str]):
        loguru.logger.debug(f'接收到的消息为{message}')


    app = QApplication([])
    s: SingnalBus = SingnalBus()
    s.lazer_gun_message.connect(show_message)
    lazer_gun = LazerGun()
    lazer_gun.start()
    app.exec()
    print('finish')
