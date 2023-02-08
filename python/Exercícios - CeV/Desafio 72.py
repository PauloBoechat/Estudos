numex = ('zero', 'um','dois', 'três', 'quatro', 'cinco', 'seis',
     'sete', 'oito', 'nove', 'dez', 'onze', 'treze', 'catorze',
      'quinze', 'dezeseis','dezesete', 'dezoito', 'dezenove', 'vinte')

while True:
    num = int(input('digite o numero que deseja ler[0/20]: '))
    if num > 20:
        print('algo deu errado, tente novamente!')
        continue
    else:
        break


print(numex[num])