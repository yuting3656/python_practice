import subprocess

"""
本範例: subprocess 基本介紹
文件連結: https://docs.python.org/3/library/subprocess.html
YouTube: https://www.youtube.com/watch?v=5XU-mAZVv4w
"""


def subprocess_show_dir():
    message = subprocess.call('dir', shell=True)
    # print(message)


if __name__ == "__main__":
    subprocess_show_dir()
