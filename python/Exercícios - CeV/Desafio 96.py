def titulo(TXT):
    print('-' * 30)
    print(TXT)
    print('-' * 30)

def area():
    x = float(input('Digite a largura do terreno: '))
    y = float(input('Digite o comprimento do terreno: '))
    print('-'*30)
    print(f'A área do terreno {x}x{y} é de {x * y}m²')


titulo('Cadastro do Tamanho do Terreno')

area()

print()
print('Obrigado por utilizar o programa!')