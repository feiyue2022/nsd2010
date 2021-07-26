# 列表[1,2,3,4,5],请使用map()函数输出[1,4,9,16,25]，并使用
# 列表推导式提取出大于10的数，最终输出[16,25]
num = [1,2,3,4,5]
print(num)
# print(type(num))
# n = list(range(1,6))
# print(n)
# print(type(n))
alist = list(map(lambda x:x**2,num))
print(alist)
a = [i for i in alist if i> 10]
print(a)