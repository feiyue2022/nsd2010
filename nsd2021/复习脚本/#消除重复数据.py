#消除重复数据
from random import randint
nums = [randint(1,10) for i in range(10)]
print(randint(1,10))
print(nums)
# [2, 4, 4, 5, 6, 8, 3, 8, 8, 9, 4, 9, 10, 1, 10, 10, 9, 9, 
# 1, 8]
print(set(nums))
# {1, 2, 3, 4, 5, 6, 8, 9, 10}
print(list(set(nums)))
# [1, 2, 3, 4, 5, 6, 8, 9, 10]
###########################################
result = []
for i in nums:
   if i not in result:
       result.append(i)
print(result)
# [2, 4, 5, 6, 8, 3, 9, 10, 1]