# #!/usr/bin/env python
# import shutil
# shutil.copyfileobj()
#
# >>> f1 = open('/etc/hosts', 'rb')
# >>> f2 = open('/tmp/hosts', 'a+b')
# >>> shutil.copyfileobj(f1,f2,4096)
# >>> f1.close()
# >>> f2.close()
#
#
# shutil.copy()
# shutil.copy2()
# shutil.move()
# >>> shutil.copy('/etc/hosts','/tmp/hosts1')
# '/tmp/hosts1'
# >>> shutil.copy2('/etc/hosts','/tmp/hosts2')
# '/tmp/hosts2'
# >>> shutil.copy2('/etc/hosts','/var/tmp/')
# '/var/tmp/hosts'
# >>> shutil.move('/var/tmp/hosts','/tmp/zhujilieibao')
# '/tmp/zhujilieibao'
#
#
#
#
# >>> shutil.copytree('/home/mark/cfg/','/tmp/immediate')
# '/tmp/immediate'
# >>> shutil.rmtree('/tmp/immediate')
#
#
#
#
# mark@mark-PC:~$ ll /tmp/hosts
# -rw-r--r-- 1 mark mark 232 6月  18 21:51 /tmp/hosts
# mark@mark-PC:~$ ll /bin/ls
# -rwxr-xr-x 1 root root 138856 9月  12  2020 /bin/ls
# >>> shutil.copymode('/bin/ls','/tmp/hosts')
# mark@mark-PC:~$ ll /tmp/hosts
# -rwxr-xr-x 1 mark mark 232 6月  18 21:51 /tmp/hosts
# mark@mark-PC:~$
#
# mark@mark-PC:~$ stat /tmp/hosts
#   文件：/tmp/hosts
#   大小：232             块：8          IO 块：4096   普通文件
# 设备：10306h/66310d     Inode：4456507     硬链接：1
# 权限：(0755/-rwxr-xr-x)  Uid：( 1000/    mark)   Gid：( 1000/    mark)
# 最近访问：2021-06-18 21:51:21.952014745 +0800
# 最近更改：2021-06-18 21:51:11.676014407 +0800
# 最近改动：2021-06-18 22:14:04.560059601 +0800
# 创建时间：-
# shutil.copystat('/bin/ls','/tmp/hosts')
# mark@mark-PC:~$ stat /tmp/hosts
#   文件：/tmp/hosts
#   大小：232             块：8          IO 块：4096   普通文件
# 设备：10306h/66310d     Inode：4456507     硬链接：1
# 权限：(0755/-rwxr-xr-x)  Uid：( 1000/    mark)   Gid：( 1000/    mark)
# 最近访问：2021-06-18 19:45:04.667961442 +0800
# 最近更改：2020-09-12 20:51:04.662037290 +0800
# 最近改动：2021-06-18 22:15:41.140062780 +0800
# 创建时间：-
#
# mark@mark-PC:~$ ll /tmp/hosts
# -rwxr-xr-x 1 mark mark 232 9月  12  2020 /tmp/hosts
# >>> shutil.chown('/tmp/hosts','root','root')
# mark@mark-PC:~$ ll /tmp/hosts
# -rwxr-xr-x 1 root root 232 9月  12  2020 /tmp/hosts
#
#
#
#
#
# ################################3
# import subprocess
# subprocess.run()
# >>> subprocess.run(['ls', '-l', 'a.sh'])
# >>> subprocess.run('ls -l a.sh',shell=True)
# >>> s = subprocess.run('ls -l a.sh',shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE)
# >>> s.args
# 'ls -l a.sh'
# >>> s.returncode
# 0
# >>> s.stdout
# b'-rw-r--r-- 1 mark mark 20 6\xe6\x9c\x88  17 22:21 a.sh\n'
# >>> s.stderr
# b''
# >>>
#
#
#
#
# >>> subprocess.getoutput('ls')
# '模板\na.sh\ncfg\ndata\nDesktop\nDocuments\nDownloads\nMusic\nPictures\nsensors\nSunloginRemote\nVideos'
# >>> s = subprocess.getoutput('ls')
# >>> s
# '模板\na.sh\ncfg\ndata\nDesktop\nDocuments\nDownloads\nMusic\nPictures\nsensors\nSunloginRemote\nVideos'
# >>> subprocess.getstatusoutput('ls')
# (0, '模板\na.sh\ncfg\ndata\nDesktop\nDocuments\nDownloads\nMusic\nPictures\nsensors\nSunloginRemote\nVideos')
# >>> s = subprocess.getstatusoutput('ls')
# >>> s[0]
# 0
# >>> s[1]
# '模板\na.sh\ncfg\ndata\nDesktop\nDocuments\nDownloads\nMusic\nPictures\nsensors\nSunloginRemote\nVideos'
# >>>




import keyword
>>> keyword.iskeyword('if')
True
>>> keyword.iskeyword('abc')
False
>>> keyword.kwlist
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
>>>

>>> type(print)
<class 'builtin_function_or_method'>
>>> print = 'abc'
>>> print
'abc'
>>> print('a')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object is not callable
>>>
