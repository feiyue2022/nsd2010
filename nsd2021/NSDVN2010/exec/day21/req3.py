#!/usr/bin/env python
import requests
from pprint import pprint

url = 'http://www.weather.com.cn/data/cityinfo/101010600.html'
r = requests.get(url)
r.encoding='utf8'
pprint(r.json())