count = 0
a = 1
while a != 0:
    a = int(input('Введите число последовательности \n'))
    if a == 0:
        break
    count += 1
print('Количество членов в последовательности равно ', count)
