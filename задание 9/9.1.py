A = []
n = 2
m = 3
for i in range(n):
    B = []
    for j in range(m):
        B.append(int(input(f'Введите [{i} , {j}] элемент матрицы ')))
    A.append(B)

for i in range(n):
    for j in range(m):
        print(A[i][j], end=' ')
    print()

max_values = []
for i in range(n):
    if A[i] == sorted(A[i]):
        max_values.append(A[i][m - 1])
    elif A[i] == sorted(A[i], reverse=True):
        max_values.append(A[i][0])
if max_values:
    print(max(max_values))
else:
    print('Строки не упорядочены')