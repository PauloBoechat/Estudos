from datetime import date


ano = date.today().year - int(input('digite o ano do seu nascimento: '))

if ano > 20:
    print('infelizmente passou do tempo para você se alistar')

elif ano < 18:
    print('ainda não está na hora de se alistar')

elif ano == 18:
    print('está na hora de se alistar')