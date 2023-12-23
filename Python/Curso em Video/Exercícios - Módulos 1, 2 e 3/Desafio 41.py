from datetime import date

idade = date.today().year - int(input('digite o ano de nascimento do nadador: '))

if idade <= 9:
    print('MIRIM')

elif idade <= 14:
    print('INFANTIL')

elif idade <= 19:
    print('JUNIOR')

elif idade <= 20:
    print('SÊNIOR')

else:
    print('MASTER')