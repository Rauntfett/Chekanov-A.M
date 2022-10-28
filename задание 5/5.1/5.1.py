def print_sqare_of_numbers():
    N = int(input('Введите N'))
    i = 1
    while pow(i, 2) < N :
        print(pow(i , 2))
        i += 1

print(print_sqare_of_numbers())