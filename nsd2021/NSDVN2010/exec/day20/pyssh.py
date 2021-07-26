#!/usr/bin/env python
import paramiko

def remote_conn(host,port,user,pwd,cmd):
    ssh_client = paramiko.SSHClient()
    #首次链接远程机器当遇到输入yes/no的步骤时，自动输入yes
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    ssh_client.connect(
        hostname=host,
        port=port,
        username=user,
        password=pwd
    )
    stdin,stdout,stderr = ssh_client.exec_command(cmd)
    #得到的对象是bits，用read()方法获取内容
    out = stdout.read()
    err = stderr.read()
    if out:
        print('%s OUT:%s' % (host,out.decode('utf8')))
    if err:
        print('%s ERR:%s' % (host,err.decode('utf8')))

    ssh_client.close()

if __name__ == '__main__':
    remote_conn('192.168.214.101',22,'root','1','ls /xxxxx')
