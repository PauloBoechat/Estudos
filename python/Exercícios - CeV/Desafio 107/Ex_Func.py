import Funções

num = int(input('Digite o preço: R$'))

print(f'A metade de R${num} é R${Funções.metade(num)}')

print(f'O dobro de R${num} é R${Funções.dobro(num)}')

print(f'Aumentando {Funções.aumentar(num)[1]}%, temos R${Funções.aumentar(num, 10)[0]}')

print(f'Diminuindo {Funções.diminuir(num, 13)[1]}%, temos R${Funções.diminuir(num, 13)[0]}')