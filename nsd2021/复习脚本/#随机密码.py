#随机密码

import random
import string
# a=string.ascii_letters+string.digits #string.ascii_letters(大小写字母)+string.ascii_digits(数字)
# key=[]
# def getKey():
# 	key=random.sample(a,8)   #random.sample 可以截取指定长度的随机数 8就是8位数
# 	keys="".join(key)           #Python join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串。
# 	return keys
# for i in range(1000):
#     print(getKey())
a = string.ascii_letters+string.digits
key = []
def getkey():
    key = random.sample(a,8)
    keys = ''.join(key)
    return keys
for i in range(5):
    print(getkey())
