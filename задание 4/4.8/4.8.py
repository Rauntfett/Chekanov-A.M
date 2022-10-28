def make_ladder():
    n = int(input('n = '))
    a=str()
    for i in range(1, n+1):
        a = a + str(i)
        print(a)

print(make_ladder())