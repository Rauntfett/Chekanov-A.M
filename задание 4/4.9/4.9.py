n = int(input('n = '))
a = 0
b = 1
c = int()
sum = 1
while n - 2 != 0:
    c = a + b
    a = b
    b = c
    sum += c
    n -= 1
print(sum)