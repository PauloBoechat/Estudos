ano = int(input('digite o ano: '))

bin = ano % 4


if bin == 0:
    print('esse ano é bissexto')
else:
    print('esse ano não é bissexto')