#!/usr/bin/env python
'''
    文件生成器
    - 通过生成器完成以下功能：
      - [x] 使用函数实现生成器
      - [x] 函数接受一个文件作为参数
      - [x] 生成器函数每次返回文件的 10 行数据
'''
def gen_block(fname):
    lines = []
    # counter = 0
    with open(fname,'r') as fobj:
        for line in fobj:
            lines.append(line)
            # counter += 1
            if len(lines) == 10:
                yield lines
                # counter = 0
                lines = []
        if lines:
            yield lines

if __name__ == '__main__':
    fname = 'passwd'
    data = gen_block(fname)
    for i in data:
        print(i)
