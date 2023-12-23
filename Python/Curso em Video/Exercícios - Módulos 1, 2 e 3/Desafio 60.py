n = int(input('digite o numero: '))
c = n
v = 1
while c > 0:
    print(' {} '.format(c), end='')
    print(' x ' if c>1 else '= ', end='')
    v *= c
    c -= 1

print(v)