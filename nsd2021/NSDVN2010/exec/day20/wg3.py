#!/usr/bin/env python
from urllib import request

import wget
import os
import re

def get_index(url,fname):
    r = request.urlopen(url)
    with open(fname,'wb') as fobj:
        fobj.write(r.read())


def get_pics(fname,patt,chatset=None):
    #charset=None,没有给定的参数，则使用系统编码作为默认编码
    res = []
    cpatt = re.compile(patt)

    with open(fname,'r',encoding=chatset) as fobj:
        for line in fobj:
            m = cpatt.search(line)
            if m:
                res.append(m.group())

    return res

def dw_pics(pics_list,path):
    for img_url in pics_list:
        wget.download(img_url,path)

if __name__ == '__main__':
    #1、下载http://www.tmooc.com网站的首页
    url = 'http://www.tmooc.cn'
    fname = 'tmooc.html'
    if os.path.exists(fname):
        os.remove(fname)
    get_index(url,fname)
    #2、找出来首页里边所有图片的url
    patt = '(http|https)://[\w\.-/]+\.(jpg|jpeg|png|gif)'
    page_code = 'utf8'
    img_list = get_pics(fname,patt,page_code)
    print(img_list)
    #3、下载图片
    path = '.\\imgs\\tmooc'
    if not os.path.exists(path):
        os.mkdir(path)
    dw_pics(img_list,path)