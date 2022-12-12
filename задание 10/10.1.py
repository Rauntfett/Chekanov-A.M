def finder_max_values(A:list[list]):
    max_values = []
    for i in range(len(matrix)):
        if A[i] == sorted(A[i]):
            max_values.append(A[i][len(matrix[i]) - 1])
        elif A[i] == sorted(A[i], reverse=True):
            max_values.append(A[i][0])
    if max_values:
        return f'Максимальное число среди упорядоченных строк равно {max(max_values)}'
    else:
        return 'Строки не упорядочены'

with open('ChekanovAM_U-224_vvod.txt', 'r', encoding='utf-8') as f:
    matrix = [list(map(int, row.split())) for row in f.readlines()]
    result = str(finder_max_values(matrix))

with open('ChekanovAM_U-224_vivod.txt', 'w', encoding='utf-8') as f:
    f.write(result)
