k = int(input('Введите число: '))

def count(k):
    nums = [ ]
    a, b = 1, 1
    for i in range(k-1):
        nums.append(a)
        a, b = b, a + b
    a, b = 0, 1
    for i in range (k):
        nums.insert(0, a)
        a, b = b, a - b
    return nums

nums = count(k)
print(count(k))