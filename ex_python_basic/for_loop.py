import platform

"""
本範例: python 基本練習
"""


def range_generate():
    for x in range(10):
        print(x)


def if_else():
    if platform.python_version() is "3.6.4":
        print("[if] version: 3.6.4")
    elif platform.python_version() is "3.7.0":
        print("[elif] version: 3.7.0")
    else:
        print("[else] version: ", platform.python_version())


if __name__ == "__main__":
    """
    到底甚麼是 __name__ == "__main__"??
    相關連結: https://stackoverflow.com/questions/419163/what-does-if-name-main-do
    """
    range_generate()
    if_else()
