#!/usr/bin/env python
'''
函数可以没有return关键字，根据函数体代码进行分析
'''
def pycp():
    with open('soul.jpg', 'rb') as f1:
        with open('a.jpg', 'a+b') as f2:
            while True:
                data = f1.read(4)
                if not data:
                    break
                f2.write(data)

pycp()