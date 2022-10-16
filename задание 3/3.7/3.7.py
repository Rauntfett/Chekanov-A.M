a = int()
def year():
    a = int(input('Введите число\n'))
    if ((a % 4 == 0) and (a % 100 != 0)) or (a % 400 == 0):
        year = 'Да'
    else:
        year = 'Нет'
    return year
print(year())