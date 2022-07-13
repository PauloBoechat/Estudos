num = int(input('digite um numero inteiro: '))
print('''escolha uma das bases para conversão:
[1] Binario
[2] Octal
[3] Hexadecimal''')
opcão = int(input('sua opção: '))

if opcão == 1:
    print('{} em Binario fica {}'.format(num, bin(num)[2:]))

elif opcão == 2:
    print('{} em Octal fica {}'.format(num, oct(num)[2:]))

elif opcão == 3:
    print('{} em Hexadecimal fica {}'.format(num, hex(num)[2:]))

else:
    print('Opção invalida')