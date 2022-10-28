def find_count_numbers_bigger_previous():
    count = 0
    a = 1
    b = 0
    while a != 0:
        a = int(input('Введите число последовательности \n'))
        if a == 0:
            break
        if a > b:
            count += 1
        b = a
    count -= 1
    return count

print(find_count_numbers_bigger_previous())
