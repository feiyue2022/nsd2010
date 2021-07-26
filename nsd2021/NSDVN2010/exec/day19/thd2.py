#!/usr/bin/env python
import subprocess
import threading

class Ping:
    def __init__(self,host):
        self.host = host
    def __call__(self):
        res = subprocess.run(
            'ping -c 2 %s &> /dev/null' % self.host,
            shell=True
        )
        if res.returncode == 0:
            print('%s is up' % self.host)
        else:
            print('%s is down' % self.host)
if __name__ == '__main__':
    ips = ['192.168.0.%s' % i for i in range(1,255)]
    for ip in ips:
        #此处target并不是函数，是类的对象，所以直接传参
        t = threading.Thread(target=Ping(ip))
        t.start()