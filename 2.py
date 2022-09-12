import math
x=float(input('x='))
y=float(input('y='))
z=float(input('z='))
s = (2 ** (-x)) * (math.sqrt(x + (abs(y) ** (1 / 4))))*(math.exp(x - 1 / math.sin(z)) ** (1 / 3))
print('s=', s)
