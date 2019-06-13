import requests
import json

"""
本範例: requests 基本介紹
文件連結: https://2.python-requests.org/en/master/
"""


class RequestClass:
    def __init__(self):
        self.json_file = []
        self.json_file_name_ch = []

    def request_machine(self):
        res = requests.get('https://taitra.online/api/country/')
        res_string = res.content.decode('utf-8')
        #  將剛剛加入的 json 編寫成 python 資料結構　 －－＞ json.loads(XXX)
        self.json_file = json.loads(res_string)
        print("什麼型別:", type(self.json_file))  # type list
        print("多大:", len(self.json_file))

    def process_json_file_get_name_ch(self):
        for i in range(len(self.json_file)):
            dict_ = {
                '中文名稱': self.json_file[i]['name_ch'],
                '國碼': self.json_file[i]['country']
            }
            self.json_file_name_ch.append(dict_)


if __name__ == "__main__":
    rs_class = RequestClass()
    rs_class.request_machine()
    rs_class.process_json_file_get_name_ch()

    print(rs_class.json_file_name_ch)

