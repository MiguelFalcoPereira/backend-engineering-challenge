from _pydecimal import Decimal
from datetime import datetime


def parse_timestamp(timestamp_str):
    # Parse the timestamp string into a datetime object
    return datetime.strptime(timestamp_str, '%Y-%m-%d %H:%M:%S.%f').replace(microsecond=0)


def format_number(num):
    decimal_num = Decimal(str(num))
    formatted_num = format(decimal_num, 'g')
    return formatted_num.rstrip('0').rstrip('.') if '.' in formatted_num else formatted_num
