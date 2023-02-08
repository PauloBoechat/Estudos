c = 1
f = s = 0
while c == 1:
    n = int(input('digite um numero [999 para parar]: '))
    if n == 999:
        c = 0
    else:
        f += n
        s += 1

print('você digitou {} numeros e a soma deles é {}!'.format(s,f))