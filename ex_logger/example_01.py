import logging
from logging.handlers import RotatingFileHandler

# datetime
from datetime import datetime as dt

"""
本範例: logger 
文件連結: https://docs.python.org/3/library/logging.html
"""


def logging_machine():
    # maxBytes to small number, in order to demonstrate the generation of multiple log files (backupCount).
    handler = RotatingFileHandler(filename='./example.log', encoding='utf-8', backupCount=3)
    # 設計 logging format
    # format: https://docs.python.org/3/library/logging.html#logging.Formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s : %(message)s')
    # 加入到 handler 裡面
    handler.setFormatter(formatter)
    global logger
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)


if __name__ == "__main__":
    logging_machine()
    logger.info('測試 {}'.format(dt.now()))
