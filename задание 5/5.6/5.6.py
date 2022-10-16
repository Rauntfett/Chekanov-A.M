count = 0
a = 1
sum=0
while a != 0:
    a = int(input('Введите число последовательности \n'))
    if a == 0:
        break
    sum += a
    count += 1
eq = sum / count
print('Среднее значение последовательности равно ', eq)
