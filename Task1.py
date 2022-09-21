lst = [int(input(f"Введите {i+1} элемент: ")) for i in range (int(input("Введите количество элементов списка: ")))]
print(lst)

sum=0

for i in range(0,len(lst)):
    if lst[i]%2!=0:
        sum=lst[i]+sum
print(sum)