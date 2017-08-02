# encoding:UTF-8
import requests
from requests.auth import HTTPBasicAuth
r = requests.get(url='http://dict.baidu.com')  # 最基本的GET请求
print(r.status_code)
# 获取返回状态

r = requests.get(url='http://dict.baidu.com/s', params={'wd': 'python'})
# 带参数的GET请求
print(r.status_code)
print(r.url)
#print(r.text)  # 打印解码后的返回数据

#json

import json
url1 = 'https://api.github.com/some/endpoint'
payload = {'some': 'data'}
headers = {'content-type': 'application/json'}

r1 = requests.post(url1, data=json.dumps(payload), headers=headers)

print(r1.status_code)
print(r1.url)
#print(r1.text)


url2='http://www.gdjdedu.net'

r2=requests.get(url2)

print(r2.status_code)
print(r2.url)
r2.encoding
print(r2.encoding)
r2.encoding='gb2312'
#print(r2.text)
urllogin='http://oa.tiexinba.net/UserLogin.asp'

s=requests.session()
html=s.get(urllogin,verify=False, allow_redirects=False)

print(html.url)
print(html.status_code)
print(html.cookies)
cooks=html.cookies
urljyj='http://oa.tiexinba.net/ShowArticle.asp?ArticleID=4813'
#res=s.get(urljyj)
res=s.get(urljyj, allow_redirects=False)
print('jyj'+str(res.status_code))
res.encoding='gb2312'
print(res.text)
print(res.history)
print(res.url)