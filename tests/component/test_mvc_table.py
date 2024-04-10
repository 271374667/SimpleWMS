import unittest
from dataclasses import dataclass

from PySide6.QtCore import Qt

from src.component.mvc_table import MVCTable, MVCTableModel, MVCTableView


@dataclass
class TestData:
    column1: str
    column2: str


class TestMVCTableModel(unittest.TestCase):
    def setUp(self):
        self.model = MVCTableModel()
        self.data = TestData("data1", "data2")
        self.headers = ["column1", "column2"]

    def test_row_count_with_no_data(self):
        self.assertEqual(self.model.rowCount(), 0)

    def test_row_count_with_data(self):
        self.model.add_row(self.data)
        self.assertEqual(self.model.rowCount(), 1)

    def test_column_count_with_no_headers(self):
        self.assertEqual(self.model.columnCount(), 0)

    def test_column_count_with_headers(self):
        self.model.set_header(self.headers)
        self.assertEqual(self.model.columnCount(), 2)

    def test_data_retrieval(self):
        self.model.add_row(self.data)
        self.model.set_header(self.headers)
        self.assertEqual(self.model.data(self.model.createIndex(0, 0)), "data1")

    def test_header_data_retrieval(self):
        self.model.set_header(self.headers)
        self.assertEqual(self.model.headerData(0, Qt.Horizontal), "column1")

    def test_add_row(self):
        self.model.add_row(self.data)
        self.assertEqual(self.model.rowCount(), 1)

    def test_clear_data(self):
        self.model.add_row(self.data)
        self.model.clear()
        self.assertEqual(self.model.rowCount(), 0)

    def test_sort_data(self):
        self.model.add_row(TestData("data3", "data4"))
        self.model.add_row(TestData("data1", "data2"))
        self.model.set_header(self.headers)
        self.model.sort(0)
        self.assertEqual(self.model.data(self.model.createIndex(0, 0)), "data1")


class TestMVCTableView(unittest.TestCase):
    def setUp(self):
        self.view = MVCTableView()
        self.model = MVCTableModel()
        self.headers = ["column1", "column2"]

    def test_set_header(self):
        self.view.set_header(self.headers)
        self.assertEqual(self.view.model().headerData(0, Qt.Horizontal), "column1")

    def test_set_model(self):
        self.view.set_model(self.model)
        self.assertEqual(self.view.model(), self.model)


class TestMVCTableController(unittest.TestCase):
    def setUp(self):
        self.controller = MVCTable()

    def test_set_dataclass(self):
        self.controller.set_dataclass(TestData)
        self.assertEqual(
            self.controller.get_model().headerData(0, Qt.Horizontal), "column1"
        )

    def test_add_row(self):
        self.controller.add_row(TestData("data1", "data2"))
        self.assertEqual(self.controller.get_model().rowCount(), 1)

    def test_clear_data(self):
        self.controller.add_row(TestData("data1", "data2"))
        self.controller.clear()
        self.assertEqual(self.controller.get_model().rowCount(), 0)

    def test_slice_data(self):
        self.controller.add_row(TestData("data1", "data2"))
        self.controller.add_row(TestData("data3", "data4"))
        self.controller.add_row(TestData("data5", "data6"))
        self.controller.add_row(TestData("data7", "data8"))
        self.controller.add_row(TestData("data9", "data10"))

        self.assertEqual(self.controller.get_model()[0], TestData("data1", "data2"))

        self.assertEqual(
            self.controller.get_model()[1:3],
            [TestData("data3", "data4"), TestData("data5", "data6")],
        )

        self.assertEqual(
            self.controller.get_model()[1:3][0], TestData("data3", "data4")
        )

        self.assertEqual(
            self.controller.get_model()[1:3][1], TestData("data5", "data6")
        )

        self.assertEqual(
            self.controller.get_model()[1:3][:2],
            [TestData("data3", "data4"), TestData("data5", "data6")],
        )

        self.assertEqual(
            self.controller.get_model()[1:3][:2][0], TestData("data3", "data4")
        )


if __name__ == "__main__":
    unittest.main()
