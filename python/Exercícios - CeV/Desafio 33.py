num1 = int(input('digite o primeiro numero: '))
num2 = int(input('digite o segundo numero: '))
num3 = int(input('digite o terceiro numero: '))

if num1 < num2 and num1 < num3:
    men = num1

if num2 < num1 and num2 < num2:
    men = num2

if num3 < num1 and num3 < num2:
    men = num3

if num1 > num2 and num1 > num3:
    mio = num1

if num2 > num1 and num2 > num3:
    mio = num2

if num3 > num1 and num3 > num2:
    mio = num3


print('O maior numero é {}, e o menor numero é {}.'.format(mio,men))