first_max = 0
second_max = 0
def finder_second_max():
    global first_max
    global second_max
    n = int(input())
    if first_max < n:
        second_max = first_max
        first_max = n
    if n == 0:
        if second_max == 0:
            return ('Последовательность состоит из одних и тех же чисел, либо в последовательности только 0')
        else:
            return (f'Второе по величине число равно {second_max}')
    return finder_second_max()


print(finder_second_max())

