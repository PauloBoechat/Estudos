a = []
pares = []
impares = []
while True:
    escolha = input('Deseja adicionar um valor a lista[S/N]: ').upper() .strip()
    if escolha == 'S':
        num = int(input('Digite o valor que será adicionado a lista: '))
        a.append(num)
    else:break

for i, v in enumerate(a):
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)

print(f'Lista completa: {a}')	
print(f'Lista de pares: {pares}')
print(f'Lista de impares: {impares}')