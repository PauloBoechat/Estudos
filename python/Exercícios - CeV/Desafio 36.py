casa = float(input('qual é o valor da casa? '))
salario = float(input('digite seu salario: '))
anos = int(input('em quantos anos vc quer pagar? '))

if casa / (anos*12) > salario * 0.3:
    print('Desculpe mas você não pode pagar por essa casa nesse prazo.')

else:
    print('você consegue pagar essa casa nesse periodo de tempo')