import unittest
from dataclasses import dataclass
from datetime import date

from src.utils.excel_handler import ExcelHandler


@dataclass
class TestData:
    name: str
    age: int
    birthday: date


class TestCodeUnderTest(unittest.TestCase):
    #  ExcelHandler can be initialized without any errors
    def test_initialize_without_errors(self):
        # Mock the following dependencies: Session, GetModelService
        # mock database session and GetModelService
        excel_handler = ExcelHandler()
        self.assertIsInstance(excel_handler, ExcelHandler)

    #  set_dataclass method sets the current dataclass and initializes header_type and header variables
    def test_set_dataclass_sets_variables(self):
        # Mock the following dependencies: Session, GetModelService
        # mock database session and GetModelService
        excel_handler = ExcelHandler()
        dataclass_mock = TestData("value1", 1, date(2021, 1, 1))
        excel_handler.set_dataclass(dataclass_mock)
        self.assertEqual(excel_handler._current_dataclass, dataclass_mock)
        self.assertEqual(
            excel_handler._header_type,
            {"name": str, "age": int, "birthday": date},
        )
        self.assertEqual(excel_handler._header, ["name", "age", "birthday"])

    #  set_data method sets the data variable
    def test_set_data_sets_variable(self):
        # Mock the following dependencies: Session, GetModelService
        # mock database session and GetModelService
        excel_handler = ExcelHandler()
        dataclass_mock = TestData("value1", 1, date(2021, 1, 1))
        excel_handler.set_data([dataclass_mock])
        self.assertEqual(excel_handler._data, [dataclass_mock])

    #  set_dataclass method raises an error if an invalid dataclass is passed
    def test_set_dataclass_invalid_dataclass(self):
        # Mock the following dependencies: Session, GetModelService
        # mock database session and GetModelService
        excel_handler = ExcelHandler()
        with self.assertRaises(TypeError):
            excel_handler.set_dataclass(str)

    #  set_dataclass method sets header_type correctly for all field types
    def test_set_dataclass_header_type(self):
        # Create an instance of ExcelHandler
        excel_handler = ExcelHandler()

        # Define a dataclass for testing
        @dataclass
        class TestData:
            name: str
            age: int
            is_active: bool

        # Set the dataclass in the ExcelHandler instance
        excel_handler.set_dataclass(TestData)

        # Check if the header_type is set correctly
        expected_header_type = {"name": str, "age": int, "is_active": bool}
        self.assertEqual(excel_handler._header_type, expected_header_type)

    #  set_data method sets data correctly for all dataclass types
    def test_set_data_correctly(self):
        # Create an instance of ExcelHandler
        excel_handler = ExcelHandler()

        # Define a dataclass for testing
        @dataclass
        class TestData:
            name: str
            age: int

        # Set the dataclass in the ExcelHandler instance
        excel_handler.set_dataclass(TestData)

        # Create some test data
        data = [TestData("John", 25), TestData("Jane", 30), TestData("Bob", 35)]

        # Set the data in the ExcelHandler instance
        excel_handler.set_data(data)

        # Check if the data is set correctly
        self.assertEqual(excel_handler._data, data)
