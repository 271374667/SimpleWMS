from dataclasses import dataclass
from datetime import datetime

import faker
from PySide6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget

from src.component.mvc_table import MVCTable
from src.component.pagination import Pagination


@dataclass
class Person:
    name: str
    age: int
    birthday: datetime


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.faker = faker.Faker(locale="zh_CN")

        self.main_layout = QVBoxLayout()
        self.table: MVCTable = MVCTable()
        self.table.set_dataclass(Person)
        self.table.add_row(Person(name="张三", age=18, birthday=datetime.now()))
        self.pagination: Pagination = Pagination()
        self.add_data_button = QPushButton("添加数据")

        self.main_layout.addWidget(self.add_data_button)
        self.main_layout.addWidget(self.table)
        self.main_layout.addWidget(self.pagination)
        self.setLayout(self.main_layout)

        # 绑定分页控件和表格
        current_page_signal = self.pagination.get_current_page_signal()
        current_page_signal.connect(self.set_current_page)
        self.pagination.set_total_pages(self.table.total_page)
        self.add_data_button.clicked.connect(self.add_data)
        self.table.per_page_count = 2

        # 添加数据

    def set_current_page(self, current_page: int):
        self.table.current_page = current_page

    def add_data(self):
        self.table.add_row(
            Person(
                name=self.faker.name(),
                age=self.faker.random_int(min=0, max=100),
                birthday=self.faker.date_time_this_century(),
            )
        )
        print(f"total_page: {self.table.total_page}")
        self.pagination.set_total_pages(self.table.total_page)


if __name__ == "__main__":
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()
