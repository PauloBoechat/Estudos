Not1 = float(input('digite sua primeira nota: '))
Not2 = float(input('digite sua segunda nota: '))

if (Not1 + Not2) / 2 >= 7:
    print('aprovado')

elif (Not1 + Not2) / 2 >= 5:
    print('recuperação')

else:
    print('reprovado')