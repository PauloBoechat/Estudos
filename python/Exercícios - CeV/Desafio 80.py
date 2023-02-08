a = []

num = int(input('Digite o valor que sera adicionado a lista: '))
a.append(num)

while True:
    escolha = str(input('deseja adicionar um número[S/N]: ')).upper() .strip()
    if escolha == 'S':
        num = int(input('Digite o valor que sera adicionado a lista: '))
        if num not in a:
            a.append(num)
            a.sort()
            print(f'O valor {num} está na posição {a.index(num)} da lista')
        else:
            escolha = input('Esse numero já foi adicionado, gostaria de adiciona-lo novamente?[S/N]: ').upper().strip()
            if escolha == 'S':
                a.append(num)
                a.sort()
                print(f'O valor {num} está na posição {a.index(num)} da lista')
    else:
        break
print(f'Esses são os números digitados: {a}')
