def sort_by_line(matrix: list[list], k: int) -> list[list]:
    i = 0
    while i != len(matrix[k]) - 1:
        j = 0
        while j < len(matrix[k]) - 1 - i:
            if matrix[k][j] > matrix[k][j + 1]:
                for z in range(len(matrix)):
                    matrix[z][j], matrix[z][j + 1] = matrix[z][j + 1], matrix[z][j]
            j += 1
        i += 1
    return matrix

D = []
m = 3
n = 3
k = int(input('Выберите номер k-й строки '))

for i in range(m):
    B = []
    for j in range(n):
        B.append(int(input(f'Введите [{i} , {j}] элемент матрицы ')))
    D.append(B)

for i in range(m):
    for j in range(n):
        print(D[i][j], end=' ')
    print()

sort_by_line(D,k)

for i in range(m):
    for j in range(n):
        print(D[i][j], end=' ')
    print()