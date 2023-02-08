s = 0
m = int(input('digite quantos numeros você vai fazer a verificação: '))
for c in range(1, m+1):
    n = int(input('digite o {}° numero: '.format(c)))
    if n % 2 == 0:
        s += n

print('você digitou {} numeros e a soma deles é {}!'.format(m,s))