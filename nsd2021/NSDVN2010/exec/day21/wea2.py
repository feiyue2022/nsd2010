#!/usr/bin/env python
import json
from pprint import pprint

def get_citycode():
    citycodes = {}
    with open('citycode.txt', 'r', encoding='utf8') as fobj:
        data = fobj.read()
        cityinfo = json.loads(data)
        items = cityinfo['城市代码']
        for item in items:
            print(item)
            provience = item['省']
            citys = item['市']
            ccs = []
            cc = {}
            for city in citys:
                cityname = city['市名']
                citycode = city['编码']
                cc[cityname] = citycode
                ccs.append(cc)
            citycodes[provience] = ccs
    pprint(citycodes)
if __name__ == '__main__':
    get_citycode()