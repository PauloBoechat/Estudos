mn = mmn = 0
a = []

randb = int(input('Digite a quantidade de números que deseja digitar: '))

for cont in range(0, randb):
    a.append(int(input('Digite um número: ')))
    if cont == 0:
        mmn = a[cont]
    if a[cont] > mn:
        mn = a[cont]
    if a[cont] < mmn:
        mmn = a[cont]

print('Os números são os seguintes: ', end='')
for cont in range(0, randb-1):
        print(f'{a[cont]},', end='')
print(f'{a[randb-1]}')

print(f'O maior número é {mn}!')
print(f'O menor número é {mmn}!')