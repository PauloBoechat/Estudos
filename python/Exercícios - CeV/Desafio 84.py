temp = []
princ = []
maxp = minp = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        maxp = minp = temp[1]
    else:
        if temp[1] > maxp:
            maxp = temp[1]
        if temp[1] < minp:
            minp = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('Deseja continuar?[S/N]: '))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'Foram cadastradas no total {len(princ)} pessoas')
print(f'O maior peso foi de {maxp}Kg, peso de ', end='')
for p in princ:
    if p[1] == maxp:
        print(f'{p[0]} ', end='')
print()
print(f'O menor peso foi de {minp}Kg, peso de ', end='')
for o in princ:
    if o[1] == minp:
        print(f'{o[0]} ', end='')
