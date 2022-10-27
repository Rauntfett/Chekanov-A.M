# -*- coding: utf-8 -*-
print('Курс Основы программирования начался')


print((16823 * 12302) % 3092)


age = int(input('Введите возраст: '))
name = input('Введите имя: ')
if 0 < age < 75 and name != 'Иван':
    if age >= 16:
        print("Поздравляем, вы поступили во ВГУИТ")
    else:
        if 16 - age == 1:
            print("Сначала нужно окончить школу! Осталось учиться:", 16 - age, "год")
        elif 2 <= 16 - age <= 4:
            print("Сначала нужно окончить школу! Осталось учиться:", 16 - age, "года")
        else:
            print("Сначала нужно окончить школу! Осталось учиться:", 16 - age, "лет")

        # if 16 - age == 1:
        #     end_year = 'год'
        # elif 2 <= 16-age <=4:
        #     end_year = 'года'
        # else:
        #     end_year = 'лет'
        # print(f'Сначала нужно окончить школу! Осталось учиться: {16 - age} {end_year}')


seconds = int(input('Введите количество секунд '))
minutes = 0
hours = 0
days = 0
if seconds >= 60:
    minutes = seconds // 60
    seconds %= 60
if minutes >= 60:
    hours = minutes // 60
    minutes %= 60
if hours >= 24:
    days = hours // 24
    hours %= 24
print(days,':',hours,':',minutes,':',seconds)


n = int(input('Введите число '))
result = n + n ** 2 + n ** 3 + n ** 4 + n ** 5
print('Результат выражения равен :', result)


x = input('Введите х ')
y = input('Введите у ')
print(x, y)
print('Заменим х и у')
c = x
x = y
y = c
print(x, y)

# x,y != y, x

number = int(input('Введите значение '))
if number % 2 == 0:
    print('Значение чётное')
else:
    print('Значение нечётное')