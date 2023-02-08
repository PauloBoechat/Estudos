from random import randint
from operator import itemgetter
from time import sleep
vr = 0

jog = {'Jogador 1': randint(0,10), 'Jogador 2' : randint(0,10), 'Jogador 3' : randint(0,10), 'Jogador 4' : randint(0,10)}

for r,k in jog.items():
    print(f'{r} recebeu {k}')
    sleep(1)
rank = sorted(jog.items(), key=itemgetter(1), reverse=True)

print('-='*10, 'Ranking', '=-'*10)
for i,v in enumerate(rank):
    print(f'{i + 1}° lugar: {v[0]} com {v[1]}.')
    sleep(1)