"""
这个模块负责让其他的View继承，实现一些一些常用的信息提示的功能
"""

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication
from qfluentwidgets import MessageBox
from qfluentwidgets.components import InfoBar, InfoBarIcon, InfoBarPosition


class MessageBaseView:
    def show_mask_dialog(self, title: str = 'Title', content: str = 'Content') -> bool:
        """显示一个遮罩式的对话框

        Args:
            title (str): 标题
            content (str): 内容

        Returns:
            bool: 是否点击了确定按钮
        """
        w = MessageBox(title, content, self)
        return bool(w.exec())

    def show_info_infobar(self, title: str = 'Title',
                          content: str = 'Content',
                          duration: int = 5000,
                          position: InfoBarPosition = InfoBarPosition.TOP_RIGHT,
                          is_closable: bool = True) -> None:
        """显示一个信息提示框

        Args:
            title (str, optional): 标题. Defaults to 'Title'.
            content (str, optional): 内容. Defaults to 'Content'.
            duration (int, optional): 持续时间. Defaults to 5000.
            position (InfoBarPosition, optional): 位置. Defaults to InfoBarPosition.TOP_RIGHT.
            is_closable (bool, optional): 是否可以被关闭. Defaults to True.
        """
        w = InfoBar(
                icon=InfoBarIcon.INFORMATION,
                title=title,
                content=content,
                orient=Qt.Vertical,  # vertical layout
                isClosable=is_closable,
                position=position,
                duration=duration,
                parent=self
                )
        w.show()

    def show_success_infobar(self, title: str = 'Title',
                             content: str = 'Content',
                             duration: int = 2000,
                             position: InfoBarPosition = InfoBarPosition.TOP_RIGHT,
                             is_closable: bool = True) -> None:
        """显示一个成功信息提示框

        Args:
            title (str, optional): 标题. Defaults to 'Title'.
            content (str, optional): 内容. Defaults to 'Content'.
            duration (int, optional): 持续时间. Defaults to 2000.
            position (InfoBarPosition, optional): 位置. Defaults to InfoBarPosition.TOP_RIGHT.
            is_closable (bool, optional): 是否可以被关闭. Defaults to True.
        """
        w = InfoBar.success(
                title=title,
                content=content,
                orient=Qt.Vertical,  # vertical layout
                isClosable=is_closable,
                position=position,
                duration=duration,
                parent=self
                )
        w.show()

    def show_warning_infobar(self, title: str = 'Title',
                             content: str = 'Content',
                             duration: int = 3000,
                             position: InfoBarPosition = InfoBarPosition.TOP_RIGHT,
                             is_closable: bool = False) -> None:
        """显示一个警告信息提示框

        Args:
            title (str, optional): 标题. Defaults to 'Title'.
            content (str, optional): 内容. Defaults to 'Content'.
            duration (int, optional): 持续时间. Defaults to 3000.
            position (InfoBarPosition, optional): 位置. Defaults to InfoBarPosition.TOP_RIGHT.
            is_closable (bool, optional): 是否可以被关闭. Defaults to False.
        """
        w = InfoBar.warning(
                title=title,
                content=content,
                orient=Qt.Vertical,  # vertical layout
                isClosable=is_closable,
                position=position,
                duration=duration,
                parent=self
                )
        w.show()

    def show_error_infobar(self, title: str = 'Title',
                           content: str = 'Content',
                           duration: int = -1,
                           position: InfoBarPosition = InfoBarPosition.TOP_RIGHT,
                           is_closable: bool = False) -> None:
        """显示一个错误信息提示框

        Args:
            title (str, optional): 标题. Defaults to 'Title'.
            content (str, optional): 内容. Defaults to 'Content'.
            duration (int, optional): 持续时间. Defaults to -1.
            position (InfoBarPosition, optional): 位置. Defaults to InfoBarPosition.TOP_RIGHT.
            is_closable (bool, optional): 是否可以被关闭. Defaults to False.
        """
        w = InfoBar.error(
                title=title,
                content=content,
                orient=Qt.Vertical,  # vertical layout
                isClosable=is_closable,
                position=position,
                duration=duration,
                parent=self
                )
        w.show()


if __name__ == '__main__':
    app = QApplication([])
    w = Demo()
    w.show()
    app.exec()
