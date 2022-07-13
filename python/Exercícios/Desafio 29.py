vl = int(input('digite a velocidade: '))

if vl > 80:
    vl = vl - 80
    mul = vl * 7
    print('Você foi multado em R${}.00'.format(mul))