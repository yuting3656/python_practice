import urllib
import urllib.request
import urllib.parse
import urllib.error
import ssl
import json

"""
本範例: urllib 搭配 class 組合的使用
文件連結: https://docs.python.org/3/library/urllib.request.html
"""


class UrlClass:
    def __init__(self, url, account, password):
        self.url = url
        self.account = account
        self.password = password

    def get_auth_token(self):
        values = {'account': '{}'.format(self.account), 'password': '{}'.format(self.password)}
        data = urllib.parse.urlencode(values)
        data = data.encode('utf-8')

        """
        opt out of certificate verification on a single connection
        文件連結: https://www.python.org/dev/peps/pep-0476/
        """
        context = ssl._create_unverified_context()

        try:
            req = urllib.request.urlopen(self.url, data, context= context)
        except urllib.error.HTTPError as e :
            print(e)
        else:
            # 用　read 讀二進位檔案
            file = req.read()
            # rep 原本就是json 檔 直接decode (從byte轉成字形)
            json_file = file.decode('utf-8')
            #  將剛剛加入的 json 編寫成 python 資料結構　 －－＞ json.loads(XXX)
            dic_json_file = json.loads(json_file)
            print(dic_json_file)
            # 可用這招讀去 value
            print(
                'success: {},'.format(dic_json_file['success']),
                'uuid: {},'.format(dic_json_file['uuid']),
                'authToken: {}'.format(dic_json_file['authToken']))


if __name__ == "__main__":
    url = 'https://spaceadmin.hyweb.com.tw/rest/auth/admin/authentication'
    account = 'sysadmin'
    password = 'sysadmin'
    url_class = UrlClass(url, account, password)

    url_class.get_auth_token()
