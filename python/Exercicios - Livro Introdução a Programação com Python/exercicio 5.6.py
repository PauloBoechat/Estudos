print('-='*5,'Gerador de tabuada', '=-'*5)
n1 = int(input('Digite o multiplicando: '))
fim = int(input('Digite o multiplicador: '))
x = 1

while x <= fim:
    print(f'{n1} x {x} = {n1*x}')
    x += 1