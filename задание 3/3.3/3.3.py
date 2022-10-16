n = int(input('Введите количество минут\n'))
def time(n):
    hours = n // 60
    while hours > 24:
        hours = hours % 24
    minutes = n % 60
    time = hours, minutes
    return time
hours, minutes = time(n)
print(hours, ':',minutes)