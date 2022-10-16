n = int()
m = int()
k = int()
def part(n, m, k):
    result = 'Нет'
    n = int(input('Введите первую сторону\n'))
    m = int (input('Введите вторую сторону\n'))
    k = int(input('Введите определённое количество долек\n'))
    for i in range(1, n+1):
        a = i * m
        if k == a:
            result = 'Да'
    for i in range(1, m+1):
        a = i * n
        if k == a:
            result = 'Да'
        return result
print(part(n, m, k))