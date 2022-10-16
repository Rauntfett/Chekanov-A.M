a = int()
b = int()
l = int()
N = int()
def length(a,b,l,N):
    a = int(input('Введите число а\n'))
    b = int(input('Введите число b\n'))
    l = int(input('Введите число l\n'))
    N = int(input('Введите число N\n'))
    length = a + 2 * N * (b + a) + 2 * l
    return length
print('Длина шнурка должна быть равна ', length(a, b, l, N))