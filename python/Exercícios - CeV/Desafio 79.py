RED   = "\033[1;31m"  
CYAN  = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"



a = []

verif = str(input(f'Deseja adicionar um valor a lista? [{GREEN}S{RESET}/{RED}N{RESET}]: ')).upper() .strip()
if verif in 'SN':
    if verif == 'S':
        a.append(int(input('Digite o valor que será adicionado a lista: ')))
        print('Número adicionado com sucesso!')
    else:
        print('nenhum valor foi adicionado!')
        exit()

while True:
    verif = str(input(f'Deseja adicionar um valor a lista? [{GREEN}S{RESET}/{RED}N{RESET}]: ')).upper() .strip()
    if verif in 'SN':
        if verif == 'S':
            while True:
                bb = int(input('Digite o valor que será adicionado a lista: '))
                if bb in a:
                    print('Esse número já está na lista! Não será adicionado!')
                    continue
                else:
                    print('Número adicionado com sucesso!')
                    a.append(bb)
                    break
        else:
            break

print(f'{CYAN}=-='*20, f'{RESET}')

a.sort()
print(f'Valores digitados: {a}')
