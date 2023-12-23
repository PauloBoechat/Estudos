from random import randint

def sorteia(lista):
    for c in range(0, 5):
        lista.append(randint(1, 10))
    print(lista, end=' ')
    
def somapares(lista):
    soma = 0
    for c in lista:
        if c % 2 == 0:
            soma += c
    print(f'A soma dos pares é {soma}')

l = list()
sorteia(l)
somapares(l)