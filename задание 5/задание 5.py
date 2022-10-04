from tkinter import Y


x = int(input('Введите х'))
y = int(input('Введите у'))
count = 1
while x < y:
    x = x*1.1
    count = count + 1
print(count)
