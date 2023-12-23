def leiaint(txt):
    while True:
        f = input(txt)
        if f.isnumeric():
            return int(f)
        
        else: print('\033[1m','\033[91m','ERRO!','\033[0m', '\033[91m','DIGITE UM NÚMERO VÁLIDO.','\033[0m')

n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
