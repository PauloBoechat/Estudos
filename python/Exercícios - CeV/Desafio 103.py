def ficha(nome='<desconhecido>',gols='0'):
    print(f'O jogador {nome} marcou {gols} gol(s) na temporada!')

#Programa Principal
n = input('Nome do jogador: ')
g = input('Número de gols: ')
if g.isnumeric():
    g = int(g)
else: g = 0

if n.strip() == '':
    ficha(gols=g)
else:ficha(n,g)