print('-'*10, 'Listagem dos preços', '-'*10)

produtos = 'lapis', 5.00, 'borracha', 3.99, 'livro', 20.00, 'caderno', 15.99, 'dicionario', 10.50

for pos in range(len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<30}', end='')
    else:
        print(f'R${produtos[pos]:>7.2f}')
print('-'*41)
