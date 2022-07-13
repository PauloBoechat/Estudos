print(10*'-', 'Bicicletario', 10*'-')
print('R$25,00 serão cobrados por aluguel')
print('')

p = int(input('digite a quantidade de horas que você deseja alugar a bicicleta: '))

print('o valor a ser pago será R${:.2f}'.format((2.5 * p) + 25))