from random import *

# F = [float(int(input("Введите число: "))) for i in range(5)]
F = [float((randint(0,15))/100) for i in range(5)]
print(F)

new_F = []
for i in range(len(F)):
    new_F.append(str(F[i]).split('.')[-1])
print(new_F)

max=new_F[0]
min=new_F[0]
for i in range(len(new_F)-1):
    if max < str(new_F[i+1]):
        max = str(new_F[i+1])
    if min > str(new_F[i+1]):
        min = str(new_F[i+1])
print(max)
print(min)

print(f"Разница максимального числа и минимального равна {int(max)-int(min)}")