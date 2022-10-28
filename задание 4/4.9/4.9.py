def find_Fibonacci():
    n = int(input('n = '))
    a = 0
    b = 1
    sum = 1
    if n == 1:
        sum = 0
    elif n == 2:
        sum = 1
    else:
        while n - 2 != 0:
            c = a + b
            a = b
            b = c
            sum += c
            n -= 1
    return sum

print(find_Fibonacci())