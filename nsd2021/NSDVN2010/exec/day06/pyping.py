#!/usr/bin/env python
'''
    调用 ping 命令
    1. 编写 ping 函数
    2. 用于测试远程主机的联通性
    3. ping 通显示：x.x.x.x:up
    4. ping 不通显示：x.x.x.x:down
'''
import sys
from subprocess import run,getstatusoutput

def ping(host):
    '''
        用Python去执行ping命令
    :param host:
    :return:
    '''
   # s = run('ping -c 2 %s &> /dev/null ' % host,shell=True)
    s = getstatusoutput('ping -c 2 %s' % host)
    # if s.returncode == 0:
    if s[0] == 0:
        return '%s:up' % host
    else:
        return '%s:down' % host

if __name__ == '__main__':
    host = sys.argv[1]
    s = ping(host)
    print(s)