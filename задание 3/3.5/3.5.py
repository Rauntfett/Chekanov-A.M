a = int()
b = int()
c = int()
def min(a, b, c):
    a = int(input('Введите первое число\n'))
    b = int(input('Введите второе число\n'))
    c = int(input('Введите третье число\n'))
    if a < b:
        min = a
    elif b < c:
        min = b
    else:
        min = c
    return min
print ('Минимальное число равно', min(a, b, c))
