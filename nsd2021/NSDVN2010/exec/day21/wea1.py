#!/usr/bin/env python
from urllib import request
import json
from pprint import pprint

def get_wea(citycode):
    url_ci = 'http://www.weather.com.cn/data/cityinfo/%s.html' % citycode
    url_sk = 'http://www.weather.com.cn/data/sk/%s.html' % citycode
    url_zs = 'http://www.weather.com.cn/data/zs/%s.html' % citycode

    urls = {'城市信息':url_ci,'城市天气实况':url_sk,'城市天气指数':url_zs}
    res = {}
    for url in urls:
        r = request.urlopen(urls[url])
        data = r.read()
        info = json.loads(data)
        res[url] = info

    return res

if __name__ == '__main__':
    citycode = '101020100'
    wea = get_wea(citycode)
    pprint(wea)