#求和 , 100以内的数字相加 
sum100 = 0
for i in range(100): sum100 +=1
counter = 1
while counter < 100 :
    sum100 += counter
    counter +=1
print(sum100)
