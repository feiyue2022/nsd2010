#!/usr/bin/env python
'''
    复制当前目录下的passwd文件，改名为mima
    Python操作文件的方式
'''
f1 = open('ls', 'rb')
f2 = open('list', 'a+b')
while True:
    data = f1.read(4)
    # if data == b'':
    #     break
    # else:
    #     f2.write(data)
    if not data:
        break
    f2.write(data)

f1.close()
f2.close()
