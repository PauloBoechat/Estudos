def linha(txt):
    print('-'*30,)
    print(txt)
    print('-'*30,)

def area():
    l = float(input('digite a largura do terreno: '))
    c = float(input('digite o comprimento do terreno: '))

    print(f'A largura de {l} e o comprimento de {c} resultam em um terreno de {l*c}m².')
    del(l)
    del(c)

def area2(l, c):
    print(f'A largura de {l} e o comprimento de {c} resultam em um terreno de {l*c}m².')


linha('Metodo 1')
area()
print()

linha('Metodo 2')
area2((float(input('digite a largura do terreno: '))), (float(input('digite o comprimento do terreno: '))))


