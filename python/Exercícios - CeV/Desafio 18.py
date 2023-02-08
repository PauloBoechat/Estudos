import math

an = float(input('digite um angulo: '))

ran = math.radians(an)
seno = math.sin(ran)
coss = math.cos(ran)
tang = math.tan(ran)

print('O valor do seno é {:.2f}'.format(seno))
print('O valor do cosseno é {:.2f}'.format(coss))
print('O valor da tangente é {:.2f}'.format(tang))