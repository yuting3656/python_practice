from datetime import datetime # 一定要這樣 import 唷!
from datetime import timedelta

"""
本範例: datetime 基本使用
文件連結: https://docs.python.org/3/library/datetime.html
"""


# timedelta 計算延遲的時間
def calculate_time():
    now = datetime.now()
    yesterday_time = now - timedelta(days=1)
    tomorrow_time = now + timedelta(days=1)
    print("昨天的此時此刻:", yesterday_time)
    print("明天的此時此刻:", tomorrow_time)
    print("現在的此時此刻:", now)


def string_parse_time():
    """
    好棒棒網站: https://www.quora.com/In-Python-what-is-the-difference-between-strftime-and-strptime
    好棒棒網站: https://stackoverflow.com/questions/14619494/how-to-understand-strptime-vs-strftime
    strftime(): convert time to string
    strptime(): convert a string to time
    """

    convert_string_to_time = datetime.strptime('2019/06/04 09:00:00', '%Y/%m/%d %H:%M:%S')
    print("convert a string to time: {}".format(convert_string_to_time.timestamp()))
    convert_time_to_string = datetime.strftime(convert_string_to_time, '%Y-%m-%d %H %M %S')
    print("convert time to string: {}".format(convert_time_to_string.split(" ")))


if __name__ == "__main__":
    calculate_time()
    string_parse_time()
