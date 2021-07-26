#!/usr/bin/env python
from urllib import request

url = 'http://www.baidu.com'
r = request.urlopen(url)        #r是一个对象
# print(r.read())                 #获取r的结果，类型为字节串
# print(r.read().decode())        #获取r的结果，类型为字符串

#保存到本地
with open('baidu.html','wb') as fobj:
    fobj.write(r.read())