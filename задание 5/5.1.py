# Задание 1
N = int(input('Введите N'))
i = 1
while i < N :
    print(pow(i , 2))
    i = i + 1

# Задание 2
a = int(input('введите а'))
while a < 2:
    print('Число а должно быть не меньше 2')
    a = int(input())
i = a
while i > 1:
    if (a % i) == 0:
        b = a % i
        i = i - 1
print(b)

# Задание 3
N = int(input('Введите N'))
x = 1
a = 2
while x < N:
    a = a * 2
print ('Число = ', a, '; Степень =', x)

# Задание 4
x = int(input('Введите х'))
y = int(input('Введите у'))
count = 0
while x < y:
    x = x*1.1
    count = count + 1
print(count)
