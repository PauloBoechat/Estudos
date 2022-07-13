import random

a1 = str(input('Digite o nome do primeiro participante: '))
a2 = str(input('Digite o nome do segundo participante: '))
a3 = str(input('Digite o nome do terceiro participante: '))
a4 = str(input('Digite o nome do quarto participante: '))

Lista = [a1, a2, a3, a4]

print('O ganhador é {}'.format(random.choice(Lista)))