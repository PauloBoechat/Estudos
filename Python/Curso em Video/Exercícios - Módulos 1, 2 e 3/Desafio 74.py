import numbers
from random import randint

m = 0
numbrs = (randint(0,10), randint(0,10), randint(0,10), randint(0,10))
print('Os valores sorteados são: ', end='')

for n in numbrs:
    m += 1
    if m == 4:
        print(f'{n} ')
    else:
        print(f'{n} ', end='')


print(f'O maior valor é {max(numbrs)}')
print(f'O menor valor é {min(numbrs)}')