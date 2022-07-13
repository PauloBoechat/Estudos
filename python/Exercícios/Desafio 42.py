l1 = float(input('digite o tamanho em cm de um lado do triangulo: '))
l2 = float(input('digite o tamanho em cm de outro lado do triangulo: '))
l3 = float(input('digite o tamanho em cm de outro lado do triangulo: '))

if l1 == l2 and l1 == l3 and l2 == l3:
    print('esse é um triangulo equilatero!')

elif l1 == l2 or l2 == l3 or l1 == l3:
    print('esse é um triangulo isósceles!')

else:
    print('esse é um triangulo escaleno!')