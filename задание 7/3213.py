a = []
j = 1
N = int(input('Введите количество элементов массива '))
x = [int(input('Введите элемент массива ')) for i in range(N)]
for i in range(N):
    for j in range(N):
        if x[i] == x[j]:
            a = a + x[i]
if len(a) == 0:
    print('Повторяющихся элементов нет')
else:
    print(a)