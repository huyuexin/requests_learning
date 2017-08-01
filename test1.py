
#coding:utf-8
import os
import urllib.request
from urllib import request
import http.cookiejar
import re

class cookie(request.BaseHandler):
    def http_request(self, req):
        simple_cookie = 'ASP.NET_SessionId=ASPSESSIONIDCACQDSQT'   #这里填自定义cookie值
        if not req.has_header('Cookie'):
            req.add_unredirected_header('Cookie', simple_cookie)  #如果header中cookie为空，则创建cookie对象并把cookie值放进去
        else:
            cookie = req.get_header('Cookie')
            req.add_unredirected_header('Cookie', simple_cookie + '; ' + cookie)  #如果header中已经存在cookie，则把自定义cookie插到已有cookie的末尾
        return req

url = 'http://www.gdjdedu.net/'
#定义cookie
mcj = http.cookiejar.MozillaCookieJar()
print(mcj)
cookiehand = urllib.request.HTTPCookieProcessor(mcj)
opener = urllib.request.build_opener(cookiehand,cookie())
opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36')]
u=opener.open(url)
print(u)
