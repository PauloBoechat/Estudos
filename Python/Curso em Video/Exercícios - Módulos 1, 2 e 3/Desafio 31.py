ds = int(input('digite a distancia em km da viagem: '))
dp = 0

if ds >= 200:
    dp = ds * 0.45
else:
    dp = ds * 0.50

print('O valor da passagem é {:.2f}'.format(dp))