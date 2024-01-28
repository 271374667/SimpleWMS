from datetime import datetime


def batch_serial_number_to_datetime(batch_serial_number: str) -> datetime:
    """将批次序号转换为时间"""
    year = int(batch_serial_number[:4])
    month = int(batch_serial_number[4:6])
    day = int(batch_serial_number[6:])
    return datetime(year=year, month=month, day=day)


def batch_serial_number_to_batch_name(batch_serial_number: str) -> str:
    """将批次序号转换为批次名称"""
    batch_number = int(batch_serial_number[-3:])
    return batch_serial_number_to_datetime(batch_serial_number).strftime(f'%Y年%m月第{batch_number:03d}批')


def convert_length12str_to_ean13(number12length: str) -> str:
    """将12位数字字符串转换为EAN13条形码"""
    if len(number12length) != 12:
        raise ValueError("The length of the input must be 12.")
    return EAN13(number12length).get_fullcode()


def convert_ean13_to_length12str(ean13: str) -> str:
    """将EAN13条形码转换为12位数字字符串"""
    if len(ean13) != 13:
        raise ValueError("The length of the input must be 13.")
    # Remove the check digit
    return ean13[:-1]


def convert_id_to_ean13(number12length: int) -> str:
    """将数字转换为EAN13条形码"""
    return convert_length12str_to_ean13(str(number12length).zfill(12))


if __name__ == '__main__':
    # print(batch_serial_number_to_datetime('202401001'))
    print(batch_serial_number_to_batch_name('202401001'))
