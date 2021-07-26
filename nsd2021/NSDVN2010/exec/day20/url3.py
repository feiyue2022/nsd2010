#!/usr/bin/env python
from urllib import request

url = 'http://www.jianshu.com'
headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0)\
     Gecko/20100101 Firefox/89.0'}
#调用Request类重新编译url
req = request.Request(url,headers=headers)
r = request.urlopen(req)
print(r.read())