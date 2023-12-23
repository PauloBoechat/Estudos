import math


from math import hypot

op = float(input('digite o cumprimento do cateto oposto: '))
ad = float(input('digite o cumprimento do cateto adiacente: '))

hip = math.hypot(op, ad)

print('O valor da hipotenusa é {:.2f}!'.format(hip))