def find_sum_factorials():
    n = int(input('n = '))
    sum = 0
    f = 1
    for i in range(1, n+1):
        f *= i
        sum += f
    return sum

print(find_sum_factorials())