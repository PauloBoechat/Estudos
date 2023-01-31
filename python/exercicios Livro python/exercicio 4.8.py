N1 = int(input('Dgite um numero: '))
N2 = int(input('Dgite outro numero: '))

OP = str(input('Indique qual operação será feita(+, -, /, x): '))

if OP == '+':
    print(f'{N1} + {N2} = {N1 + N2}')
    
elif OP == '-':
    print(f'{N1} - {N2} = {N1 - N2}')

elif OP == 'x':
    print(f'{N1} x {N2} = {N1 * N2}')

elif OP == '÷' or OP == '/':
    print(f'{N1} ÷ {N2} = {N1 / N2}')

else: 
    print('Essa categoria é invalida! Tente novamente!')