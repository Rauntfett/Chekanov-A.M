def print_min_devider():
    a = int(input('введите а'))
    while a < 2:
        print('Число а должно быть не меньше 2')
        a = int(input())
    i = a
    while i > 1:
        if (a % i) == 0:
            b = i
        i -= 1
    return b

print(print_min_devider())