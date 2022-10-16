max = 0
count = 0
b = 0
a = 1
while a != 0:
    a = int(input('Введите число последовательности \n'))
    if a == 0:
        break
    if a == b:
        count += 1
        if count > max:
            max = count
    b = a
print('Наибольшее число подряд идущих равных элементов равно', max)