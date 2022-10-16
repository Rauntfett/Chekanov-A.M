a = int(input('Введите номер столбца первой клетки\n'))
b = int(input('Введите номер строки первой клетки\n'))
x = int(input('Введите номер столбца второй клетки\n'))
y = int(input('Введите номер строки второй клетки\n'))
def colour_cells(a, b, x, y):
    if a % 2 == 1:
        if b % 2 == 1:
            cell1 = 'Чёрная'
        else:
            cell1 = 'Белая'
    else:
        if b % 2 == 1:
            cell1 = 'Белая'
        else:
            cell1 = 'Чёрная'

    if x % 2 == 1:
        if y % 2 == 1:
            cell2 = 'Чёрная'
        else:
            cell2 = 'Белая'
    else:
        if y % 2 == 1:
            cell2 = 'Белая'
        else:
            cell2 = 'Чёрная'
    return [cell1, cell2]

cell1, cell2 = colour_cells(a, b, x, y)
if cell1 == cell2:
    print('Да')
else:
    print('Нет')