from dataclasses import dataclass
from datetime import datetime

import faker
from PySide6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget

from src.component.mvc_table_with_pagination import MVCTableWithPagination


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
        self.table: MVCTableWithPagination = MVCTableWithPagination()
        self.table.set_dataclass(Person)
        self.table.add_row(Person(name="张三", age=18, birthday=datetime.now()))
        self.add_data_button = QPushButton("添加数据")

        self.main_layout.addWidget(self.add_data_button)
        self.main_layout.addWidget(self.table)
        self.setLayout(self.main_layout)

        self.add_data_button.clicked.connect(self.add_data)

    def add_data(self):
        self.table.add_row(
            Person(
                name=self.faker.name(),
                age=self.faker.random_int(min=0, max=100),
                birthday=self.faker.date_time_this_century(),
            )
        )


if __name__ == "__main__":
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()
