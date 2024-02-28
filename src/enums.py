from enum import Enum, auto


class BasicSearchCombboxOperationEnum(Enum):
    Equal = 0
    Greater = auto()
    Less = auto()


class TimeFilterEnum(Enum):
    Day = 0
    Week = auto()
    FiftenDays = auto()
    Month = auto()
    All = auto()
