sl = float(input('digite o valor do seu salario: '))

if sl >= 1250.00:
    sl = sl + (sl * 0.1)
    print('seu salario agora é de R${}'.format(sl))
else:
    sl = sl + (sl * 0.15)
    print('seu salario agora é de R${}'.format(sl))