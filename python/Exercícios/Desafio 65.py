c = a = x = o = 0

while c == 0:
    n = int(input('digite um numero: '))
    a += 1
    x += n
    if n > o:
        o = n
    p = input('deseja continuar? [S/N]: ').upper() .strip() [0]
    if p == 'N':
        c = 1


print('Você digitou {} numeros e a média foi {:.2f}'.format(a, x/a))
print('O maior numero foi {}!'.format(o))
