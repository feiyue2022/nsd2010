#!/usr/bin/env python
# def pd(x,y):
#     if x > y:
#         return  x
#     elif x < y:
#         return y
#     else:
#         return 0
def pd(x,y):
    if x > y:
        return x
    else:
        if x < y:
            return y
        else:
            return 0

lpd = lambda x,y:       x  if x > y   else  (y if x < y   else 0)


print(lpd(1,4))
print(lpd(3,2))
print(lpd(4,4))