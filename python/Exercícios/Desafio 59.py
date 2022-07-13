n1 = float(input('digite o primeiro numero: '))
n2 = float(input('digite o segundo numero: '))

opc = 0
while opc != 5:
    print('''    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa''')
    opc = int(input('digite a opção selecionada: '))

    if opc == 1:
        print('{} + {} = {}'.format(n1, n2, n1+n2))
        print('-' * 25)
    elif opc == 2:
        print('{} x {} = {}'.format(n1, n2, n1*n2))
        print('-' * 25)
    elif opc == 3:
        if n1 > n2:
            print('{} é o maior numero!'.format(n1))
            print('-' * 25)
        else:
            print('{} é o maior numero!'.format(n2))
            print('-' * 25)
    elif opc == 4:
        n1 = int(input('digite o primeiro valor: '))
        n2 = int(input('digite o segundo valor: '))
        print('-' * 25)
    elif opc == 5:
        print('finalizando...')
    else:
        print('algo deu errado, tente novamente')
        print('-' * 25)


print('-'*50)
print('fim do programa, tenha um bom dia')