import threading

"""
本範例: threading timer 使用
stack overflow: https://stackoverflow.com/questions/3393612/run-certain-code-every-n-seconds/13151299
文件連結: https://docs.python.org/3/library/threading.html#timer-objects
"""


def threading_machine():
    """" 每兩秒 print 一次 """
    global counter
    timer = threading.Timer(2, threading_machine)
    print('threading machine says hello~~')
    print('counter: {}'.format(counter))
    timer.start()
    if counter == 10:
        timer.cancel()
    counter += 1


if __name__ == "__main__":
    counter = 0
    threading_machine()
