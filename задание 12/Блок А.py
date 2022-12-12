# Блок А, №1
def func(x, n):
    if n == 0:
        return 1
    return func(x, n-1)*x/n

print(func(4, 5))