#!/usr/bin/env python
import requests

url = 'https://img0.baidu.com/it/u=3101694723,748884042&fm=26&fmt=auto&gp=0.jpg'
r = requests.get(url)
#bytes流用.content属性匹配
print(r.content)

with open('cat.jpg','wb') as fobj:
    fobj.write(r.content)