#!/usr/bin/env python
from urllib import request

url='http://bpic.588ku.com/element_origin_min_pic/16/10/29/2ac8e99273bc079e40a8dc079ca11b1f.jpg'
r = request.urlopen(url)
with open('imgs/a.jpg','wb') as fobj:
    fobj.write(r.read())