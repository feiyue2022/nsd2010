#!/usr/bin/env python
from urllib import request
from urllib import error

url1 = 'http://192.168.214.101/abc'
url2 = 'http://192.168.214.101/bbc'
url3 = 'http://192.168.214.101/'
#调用error.HTTPError类，捕获所有的http异常请求
for i in url1,url2,url3:
    try:
        r = request.urlopen(i)
    except error.HTTPError as e:
        print('error', e)