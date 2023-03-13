def fatorial(n,opl=True):
    fat = 1
    for c in range(n, 0, -1):
        fat *= c
        if opl == True:
            print(c, end=' x ')
    if opl == True:
        print(f'= {fat}')
    print(f'O fatorial de {n} é {fat}')

n = int(input('Digite o valor que será fatorado: '))
opl = input('Deseja ver o processo(S/N): ').upper()
if opl == 'S': opl = True
else: opl = False

fatorial(n,opl)