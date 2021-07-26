#!/usr/bin/env python
from urllib import request
import requests

url = 'http://www.baidu.com'
# r = request.urlopen(url)
# data = r.read()
# print(data.decode())

r = requests.get(url)
r.encoding='utf8'
#文本格式用.text属性匹配
print(r.text)
# with open('baidu.html','w') as fobj:
#     fobj.write(r.text)