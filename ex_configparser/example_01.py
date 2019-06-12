import configparser

"""
本範例: configparser 使用
stack overflow: https://stackoverflow.com/questions/3393612/run-certain-code-every-n-seconds/13151299
文件連結: https://docs.python.org/3/library/threading.html#timer-objects
"""


def config_machine():
    config = configparser.ConfigParser()
    config.read("./config.ini")

    # example_01
    host = config.get('example_01', 'host')
    port = config.get('example_01', 'port')
    print("example_01: [ host: %s, port: %s ]" % (host, port))
    # example_02
    name = config.get('example_02', 'name').strip('"')
    address = config.get('example_02', 'address').strip('"')
    print("example_02: [ name: {}, address: {} ]".format(name, address))


if __name__ == "__main__":
    config_machine()
