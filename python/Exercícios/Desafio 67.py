while True:
    print('-'*76)
    n = int(input('quer a tabuada de qual valor(digite um valor negativo para parar)? '))
    print('-'*76)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')
print('obrigado por me utilizar, volte sempre')