from random import *

lst = [randint(0,25) for i in range(10)]
print(lst)
print(len(lst))

sum = []

for i in range(int(len(lst)/2)):
    sum.append(lst[i]+lst[-1-i])
print(sum)