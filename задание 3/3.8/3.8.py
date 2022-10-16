a = int()
b = int()
c = int()
def equal(a, b, c):
    a = int(input('Введите первое число'))
    b = int(input('Введите второе число'))
    c = int(input('Введите третье число'))
    if a == b and a == c:
        equal = 3
    elif a == b or a == c:
        equal = 2
    else:
        equal = 0
    return equal
print(equal(a, b, c))