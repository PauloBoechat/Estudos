n1 = int(input('digite o numero que será multiplicado: '))
n2 = int(input('digite numero que vai multiplicar: '))
print('resultado:')

for c in range(1, n2+1):
    print('{} x {} = {}'.format(n1, c, n1 * c))
