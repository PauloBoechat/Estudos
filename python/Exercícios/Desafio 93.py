info = dict()
tot = list()

info['Nome'] = str(input('Nome: '))
Partidas = int(input('Quantidade de Partidas: '))

for c in range(0, Partidas):
    tot.append(int(input(f'Quantidade de gols na partida {c + 1}°:')))

info['Gols'] = tot[:]
info['Total'] = sum(tot)

print('-'*30)

for k,v in info.items():
    print(f'{k} tem o valor {v}: ')
print(f'O jogador {info["Nome"]} jogou {Partidas} partidas.')

print('-'*30)
for c in range(0, Partidas):
    print(f'No jogo {c + 1} ele marcou {tot[c]} gol(s).')