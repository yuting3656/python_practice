import urllib.parse
import urllib.request
import ssl
import json

"""
本範例: urllib 基本使用
文件連結: https://docs.python.org/3/library/urllib.request.html
"""


url = 'https://spaceadmin.hyweb.com.tw/rest/auth/admin/authentication'

# prepare the data
values = {'account': 'sysadmin', 'password': 'sysadmin'}
data = urllib.parse.urlencode(values)
data = data.encode('utf-8')

"""
opt out of certificate verification on a single connection
文件連結: https://www.python.org/dev/peps/pep-0476/
"""
context = ssl._create_unverified_context()

req = urllib.request.urlopen(url, data, context=context)

# 先將 req存起來　避免不見！
# 用　read 讀二進位檔案
file = req.read()

# 直接用 byte (print)寫出來
print(file)

# 將資料編寫成 json　字串 －－＞ json.dumps(XXX)

# rep 原本就是json檔 直接decode (從byte轉成字形)
json_file = file.decode('utf-8')
print(json_file)
print(type(json_file))

print('=========== getting json value============')

#  將剛剛加入的 json 編寫成 python 資料結構　 －－＞ json.loads(XXX)
dic_json_file = json.loads(json_file)
# 可用這招讀去 value
print(dic_json_file['success'], dic_json_file['uuid'], dic_json_file['authToken'])

