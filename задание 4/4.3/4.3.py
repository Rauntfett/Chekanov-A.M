a = int(input('a = '))
b = int(input('b = '))
for i in range(a, b - 1, -1):
    if i % 2 == 1:
        print(i)