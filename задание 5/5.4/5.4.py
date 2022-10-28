def count_way():
    x = int(input('Введите х '))
    y = int(input('Введите у '))
    count = 0
    while x < y:
        x = x*1.1
        count += 1
    return count

print(count_way())
