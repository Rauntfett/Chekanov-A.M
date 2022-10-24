def swap():
    a = [int(input('Введите элемент массива ')) for i in range(15)]
    print(a)
    for i in range(15):
        if a[i] < 10:
            a[i] = 0
        elif a[i] > 20:
            a[i] = 1
    print(a)
    return a
