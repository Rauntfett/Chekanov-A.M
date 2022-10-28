def count_all_numbers_before_0():
    count = 0
    a = 1
    while a != 0:
        a = int(input('Введите число последовательности \n'))
        if a == 0:
            break
        count += 1
    return count

print(count_all_numbers_before_0())
