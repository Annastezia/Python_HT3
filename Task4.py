num = int(input("Введите десятичное число: "))
print(num)

num2 = [ ]
while num >= 1:
    if num%2==0:
        num2.append(0)
        num = num/2
    elif num%2==1:
        num=num//2
        num2.append(1)
num2.reverse()
print(" ".join(map(str,num2)))