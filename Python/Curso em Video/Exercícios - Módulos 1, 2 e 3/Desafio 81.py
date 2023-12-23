a = []
count = 0
while True:
    escolha = input('Deseja adicionar um valor a lista[S/N]: ').upper() .strip()
    if escolha == 'S':
        num = int(input('Digite o valor que será adicionado a lista: '))
        count += 1
        a.append(num)
    else:break

a.sort(reverse=True)
print(f'Você digitou {count} elementos')
print(f'Sua lista em decrescente fica: {a}')
if 5 in a:
    print('Na sua lista existe um ou mais número(s) 5!')
else:
    print('Na sua lista não há o número 5!')