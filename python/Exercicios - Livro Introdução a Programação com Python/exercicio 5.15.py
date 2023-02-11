tot = 0
while True:
    cod = int(input('Digite o código do produto(0 para cancelar): ')) 
    if cod <= 0:
        break
    quant = int(input('Digite a quantidade de produtos que deseja: '))
    if cod == 1:
        print()
        print('O valor deste produto é de R$0,50!')
        print(f'Val. Total: R${0.5 * quant:.2f}')
        print()
        tot = tot + 0.5 * quant
    elif cod == 2:
        print()
        print('O valor deste produto é de R$1,00!')
        print(f'Val. Total: R${1.0 * quant:.2f}')
        print()
        tot = tot + 1.0 * quant
    elif cod == 3:
        print()
        print('O valor deste produto é de R$4,00!')
        print(f'Val. Total: R${4.0 * quant:.2f}')
        print()
        tot = tot + 4.0 * quant
    elif cod == 5:
        print()
        print('O valor deste produto é de R$7,00!')
        print(f'Val. Total: R${7.0 * quant:.2f}')
        print()
        tot = tot + 7.0 * quant
    elif cod == 9:
        print()
        print('O valor deste produto é de R$8,00!')
        print(f'Val. Total: R${8.0 * quant:.2f}')
        print()
        tot = tot + 8.0 *quant
    else: print('Código inválido')

print('O total foi de R${:.2f}'.format(tot))