preco = float(input('digite o preço: '))
print('1: À vista, 2: À vista no cartão, 3: 2x no cartão, 4: 3x ou mais no cartão')
cdp = int(input('digite o metodo do pagamento: '))

if cdp == 1:
    print('R${}'.format(preco - (preco * 0.1)))

elif cdp == 2:
    print('R${}'.format(preco - (preco * 0.05)))

elif cdp == 3:
    print('R${}'.format(preco))

elif cdp == 4:
    print('R${}'.format())

else:
    print('metodo de pagamento não reconhecido')