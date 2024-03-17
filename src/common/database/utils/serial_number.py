from datetime import datetime


def sort_serial_number(serial_number_list: list[str]) -> list[str]:
    # 使用内置的sorted函数进行排序，key参数用于指定排序的依据
    # 这里我们先按照年份和月份排序，然后再按照序号排序
    # 因为我们希望年份和月份最新的以及序号大的排在前面，所以使用了负数
    sorted_list = sorted(serial_number_list, key=lambda x: (-int(x[:6]), -int(x[6:])))
    return sorted_list


def gen_serial_number(serial_number: int) -> str:
    today = datetime.today()
    return f"{today.year}{today.month:02d}{serial_number:03d}"


def parser_serial_number_to_int(serial_number: str) -> int:
    if len(serial_number) != 9:
        raise ValueError(f"序列号长度不正确，必须为9位，当前长度为{len(serial_number)}")
    return int(serial_number[-3:])
