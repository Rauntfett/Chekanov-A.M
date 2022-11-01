def find_count_of_numbers(a, b, c: int) -> int:
    count = 0
    N = int(input('Введите правую границу отрезка '))
    while N > 231 or N < 210:
        N = int(input('Число должно быть меньше 231 и больше 210, введите число заново: '))
    for elements in range(100, N+1):
        if (a == elements % 10) and (b == (elements // 10) % 10) and (c == (elements // 100)):
            count += 1
        elif (b == elements % 10) and (c == (elements // 10) % 10) and (a == (elements // 100)):
            count += 1
        elif (c == elements % 10) and (a == (elements // 10) % 10) and (b == (elements // 100)):
            count += 1
    return count

print(find_count_of_numbers(1, 0, 1))

