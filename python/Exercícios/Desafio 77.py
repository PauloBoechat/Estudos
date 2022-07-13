palavras = 'APRENDER', 'COCADA', 'MINECRAFT', 'MERCADO'

for n in palavras:
    print(f'\nNa palavra {n} temos as seguintes vogais: ', end='')
    for letra in n:
        if letra in 'AEIOU':
            print(letra, end=' ')