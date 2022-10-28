def print_max_degree_of_2():
    N = int(input('Введите N\n'))
    x = 1
    a = 2
    while x < N:
        a = a * 2
        x += 1
    print ('Число = ', a, '; Степень =', x)

print(print_max_degree_of_2())