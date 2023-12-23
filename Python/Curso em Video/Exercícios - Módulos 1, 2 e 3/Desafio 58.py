from random import randint


n = randint(0, 10)

u = int(input('advinhe o numero de 0 a 10:'))
c = 1

while u != n:
    u = int(input('ops, parece que você errou, tente novamente: '))
    c += 1

print('foram necessarias {} tentativas para acertar o numero!'.format(c))