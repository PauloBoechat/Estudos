import random


num = random.randint(0, 5)

usnum = int(input('adivinhe o numero de 0 a 5: '))

if usnum > 5:
    print('Eu acho que esse numero é grande de mais')
else:
    if usnum == num:
        print('parabéns, você acertou')
    else:
        print('você errou, o numero é {}'.format(num))