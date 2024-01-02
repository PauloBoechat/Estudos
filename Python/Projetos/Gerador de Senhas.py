from random import choice
import string
senha = ''


while True:
    NumDC = input('digite a quantidade de caracteres da senha: ')
    Ver = NumDC.isnumeric()
    if Ver == True:
        NumDC = int(NumDC)
        break
    else:
        print('Algo deu errado, tente novamente!')
        continue

while True:
    LetM = input('Precisa de letra maiúscula?[S/N]: ').upper() .strip() [0]
    if LetM in 'SN':
        break
    else:
        print('Algo deu errado, tente novamente!')
        continue

while True:
    Letm = input('Precisa de letra minúscula?[S/N]: ').upper() .strip() [0]
    if Letm in 'SN':
        break
    else:
        print('Algo deu errado, tente novamente!')
        continue

while True:
    NumSN = input('Precisa de números?[S/N]: ').upper() .strip() [0]
    if NumSN in 'SN':
        break
    else:
        print('Algo deu errado, tente novamente!')
        continue

while True:
    SimB = input('Precisa de símbolos?[S/N]: ').upper() .strip() [0]
    if SimB in 'SN':
        break
    else:
        print('Algo deu errado, tente novamente!')
        continue


if Letm == 'S':
    valores = string.ascii_lowercase

if LetM == 'S':
    valores += string.ascii_uppercase

if NumSN == 'S':
    valores += string.digits

if SimB == 'S':
    valores += string.punctuation

for i in range(NumDC):
    senha += choice(valores)

print(senha)