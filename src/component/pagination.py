from typing import Optional, Union

import loguru
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QIntValidator
from PySide6.QtWidgets import QHBoxLayout, QWidget
from qfluentwidgets import ToolTipFilter
from qfluentwidgets.components import BodyLabel, LineEdit, PushButton, ToggleButton


class Pagination(QWidget):
    current_page_changed = Signal(int)
    error_message = Signal(str)

    def __init__(
        self,
        parent=None,
        total_pages: Optional[int] = 1,
        max_button_number: int = 10,
        left_button_number: int = 4,
        right_button_number: int = 4,
    ):
        super().__init__(parent=parent)

        if max_button_number < left_button_number + right_button_number + 1:
            raise ValueError(
                "max_button_number must be greater than left_button_number + right_button_number + 1"
            )

        self.total_pages = total_pages
        self.max_button_number = max_button_number
        self.left_button_number = left_button_number
        self.right_button_number = right_button_number
        self.current_page = 1

        self.main_layout = QHBoxLayout(self)
        self.button_layout = QHBoxLayout()
        self.main_layout.addLayout(self.button_layout)

        self.buttons: list[Union[ToggleButton, BodyLabel]] = []

        self.lineEdit = LineEdit(self)
        self.lineEdit.setToolTip("输入页码后按回车跳转")
        self.lineEdit.setPlaceholderText("页码")
        self.lineEdit.setFixedWidth(100)
        # 设置只能输入数字
        self.lineEdit.setValidator(QIntValidator())
        self.lineEdit.returnPressed.connect(self._on_line_edit_return_pressed)

        self.confirm_button = PushButton("跳转", self)
        self.confirm_button.clicked.connect(self._on_line_edit_return_pressed)

        # 当total_pages为None或者小于1时，隐藏分页组件
        if not total_pages or total_pages <= 1:
            self.hide()
            self.lineEdit.hide()
            self.confirm_button.hide()

        self.main_layout.addWidget(self.lineEdit)
        self.main_layout.addWidget(self.confirm_button)
        self._update_buttons()

        for each in self.findChildren(QWidget):
            each.installEventFilter(ToolTipFilter(each, 200))

    def get_current_page(self) -> int:
        return self.current_page

    def get_total_pages(self) -> int:
        return self.total_pages

    def get_max_button_number(self) -> int:
        return self.max_button_number

    def get_left_button_number(self) -> int:
        return self.left_button_number

    def get_right_button_number(self) -> int:
        return self.right_button_number

    def get_current_page_signal(self) -> Signal:
        return self.current_page_changed

    def get_error_message_signal(self) -> Signal:
        return self.error_message

    def set_current_page(self, page: int) -> None:
        if page < 1 or page > self.total_pages:
            raise ValueError("page must be greater than 0 and less than total_pages")

        self._update_page(page)

    def set_total_pages(self, total_pages: int) -> None:
        loguru.logger.debug(total_pages)
        if total_pages <= 1:
            self.hide()
            self.setVisible(False)
            self.lineEdit.hide()
            self.confirm_button.hide()
        else:
            self.show()
            self.setVisible(True)
            self.lineEdit.show()
            self.confirm_button.show()

        self.total_pages = total_pages
        self._update_buttons()

    def set_max_button_number(self, max_button_number: int) -> None:
        if max_button_number < self.left_button_number + self.right_button_number + 1:
            raise ValueError(
                "max_button_number must be greater than left_button_number + right_button_number + 1"
            )

        self.max_button_number = max_button_number
        self._update_buttons()

    def set_left_button_number(self, left_button_number: int) -> None:
        if left_button_number + self.right_button_number + 1 > self.max_button_number:
            raise ValueError(
                "left_button_number + right_button_number + 1 must be less than max_button_number"
            )

        self.left_button_number = left_button_number
        self._update_buttons()

    def set_right_button_number(self, right_button_number: int) -> None:
        if self.left_button_number + right_button_number + 1 > self.max_button_number:
            raise ValueError(
                "left_button_number + right_button_number + 1 must be less than max_button_number"
            )

        self.right_button_number = right_button_number
        self._update_buttons()

    def _update_buttons(self):
        for button in self.buttons:
            self.button_layout.removeWidget(button)
            button.deleteLater()
        self.buttons.clear()

        start_page = max(1, self.current_page - self.left_button_number)
        end_page = min(self.total_pages, self.current_page + self.right_button_number)

        # If total_pages is less than max_button_number, show all buttons
        if self.total_pages <= self.max_button_number:
            start_page = 1
            end_page = self.total_pages
        elif end_page - start_page + 1 < self.max_button_number:
            diff = self.max_button_number - (end_page - start_page + 1)
            if start_page - diff > 1:
                start_page -= diff
            else:
                end_page += diff

        # Ensure start_page and end_page are within valid range
        start_page = max(1, start_page)
        end_page = min(self.total_pages, end_page)

        if end_page == 1:
            return

        if start_page > 1:
            self._add_button(1)
            if start_page >= 2:
                self._add_label("...")
            start_page += 1

        for page in range(start_page, end_page + 1):
            # Check if the number of buttons has reached total_pages
            if len(self.buttons) >= self.total_pages:
                break
            self._add_button(page)

        if end_page < self.total_pages:
            if end_page < self.total_pages - 1:
                self._add_label("...")
            self._add_button(self.total_pages)

    def _add_button(self, page):
        button = ToggleButton(str(page), self)
        button.clicked.connect(lambda: self._on_button_clicked(button))
        self.button_layout.addWidget(button)
        self.buttons.append(button)
        if page == self.current_page:
            button.setChecked(True)

    def _add_label(self, text):
        label = BodyLabel(text, self)
        label.setAlignment(
            Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter
        )
        self.button_layout.addWidget(label)
        self.buttons.append(label)

    def _on_button_clicked(self, button: ToggleButton):
        page = int(button.text())
        if page == self.current_page:
            loguru.logger.debug(f"已经是第{page}页")
            button.setChecked(True)
        else:
            self._update_page(page)

    def _on_line_edit_return_pressed(self):
        text = self.lineEdit.text()
        if text.isdigit():
            page = int(text)
            if 1 <= page <= self.total_pages:
                self._update_page(page)
            else:
                loguru.logger.debug(f"输入的页码{page}超出范围")
                self.error_message.emit("输入的页码超出范围")
        else:
            loguru.logger.debug(f"输入的页码{text}不是数字")
            self.error_message.emit("输入的页码不是数字")

    def _update_page(self, page):
        self.current_page = page
        self._update_buttons()
        self.current_page_changed.emit(page)


if __name__ == "__main__":
    import sys

    from PySide6.QtWidgets import QApplication

    app = QApplication(sys.argv)
    window = Pagination(total_pages=1)
    window.current_page_changed.connect(lambda page: print(f"当前页码为: {page}"))
    print(window.get_total_pages())
    # window.set_total_pages(10)
    # window.set_current_page(50)
    window.set_total_pages(100)

    window.show()
    sys.exit(app.exec())
