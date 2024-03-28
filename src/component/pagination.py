from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QIntValidator
from PySide6.QtWidgets import QHBoxLayout, QWidget
from qfluentwidgets.components import BodyLabel, LineEdit, ToggleButton, PushButton
from qfluentwidgets import ToolTipFilter


class Pagination(QWidget):
    current_page_changed = Signal(int)

    def __init__(
        self,
        total_pages,
        max_button_number=10,
        left_button_number=4,
        right_button_number=4,
    ):
        super().__init__()
        if max_button_number < left_button_number + right_button_number + 1:
            raise ValueError(
                "max_button_number must be greater than left_button_number + right_button_number + 1"
            )
        if total_pages < 1:
            raise ValueError("total_pages must be greater than 0")

        self.total_pages = total_pages
        self.max_button_number = max_button_number
        self.left_button_number = left_button_number
        self.right_button_number = right_button_number
        self.current_page = 1

        self.main_layout = QHBoxLayout(self)
        self.button_layout = QHBoxLayout()
        self.main_layout.addLayout(self.button_layout)

        self.buttons: list[ToggleButton | BodyLabel] = []

        self.lineEdit = LineEdit(self)
        self.lineEdit.setToolTip("输入页码后按回车跳转")
        self.lineEdit.setPlaceholderText("页码")
        self.lineEdit.setFixedWidth(100)
        # 设置只能输入数字
        self.lineEdit.setValidator(QIntValidator())
        self.lineEdit.returnPressed.connect(self._on_line_edit_return_pressed)

        self.confirm_button = PushButton("跳转", self)
        self.confirm_button.clicked.connect(self._on_line_edit_return_pressed)

        self.main_layout.addWidget(self.lineEdit)
        self.main_layout.addWidget(self.confirm_button)
        self._update_buttons()
        
        for each in self.findChildren(QWidget):
                    each.installEventFilter(ToolTipFilter(each, 200))

    def _update_buttons(self):
        for button in self.buttons:
            self.button_layout.removeWidget(button)
            button.deleteLater()
        self.buttons.clear()

        start_page = max(1, self.current_page - self.left_button_number)
        end_page = min(self.total_pages, self.current_page + self.right_button_number)

        # Ensure that the number of buttons is always self.max_button_number
        if end_page - start_page + 1 < self.max_button_number:
            diff = self.max_button_number - (end_page - start_page + 1)
            if start_page - diff > 1:
                start_page -= diff
            else:
                end_page += diff

        if start_page > 1:
            self._add_button(1)
            if start_page > 2:
                self._add_label("...")
            start_page += 1

        for page in range(start_page, end_page + 1):
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
            print(f"已经是第{page}页")
            button.setChecked(True)
        else:
            self.current_page = page
            self._update_buttons()
            self.current_page_changed.emit(page)

    def _on_line_edit_return_pressed(self):
        text = self.lineEdit.text()
        if text.isdigit():
            page = int(text)
            if 1 <= page <= self.total_pages:
                self.current_page = page
                self._update_buttons()
                self.current_page_changed.emit(page)
            else:
                print(f"输入的页码{page}超出范围")
        else:
            print("请输入有效的页码")

    def set_current_page(self, page: int):
        if page < 1 or page > self.total_pages:
            raise ValueError("page must be greater than 0 and less than total_pages")
        
        self.current_page = page
        self._update_buttons()
        self.current_page_changed.emit(page)


if __name__ == "__main__":
    import sys

    from PySide6.QtWidgets import QApplication

    app = QApplication(sys.argv)
    window = Pagination(100)
    window.current_page_changed.connect(lambda page: print(f"当前页码为: {page}"))
    window.set_current_page(50)
    
    window.show()
    sys.exit(app.exec())
