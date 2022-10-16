a = int(input('Введите длину первого катета\n'))
b = int(input('Введите длину второго катета\n'))
def square(a,b):
    square = 1/2 * a * b
    return square
print('Площать прямоугольного треугольника равна', square(a, b))