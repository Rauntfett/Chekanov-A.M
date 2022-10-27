import math
x=float(input('x=')) # x = 3.981 * 10 ** 2
y=float(input('y=')) # y = -1.625 * 10 ** 3
z=float(input('z=')) # z = 0.512
s = (2 ** (-x)) * (math.sqrt(x + (abs(y) ** (1 / 4))))*(math.exp(x - 1 / math.sin(z)) ** (1 / 3))
print('s=', s)
