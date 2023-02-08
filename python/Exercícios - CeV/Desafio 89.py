lista = []
dadosps = []
while True:
    dadosps.append(input('Nome: '))
    dadosps.append(float(input('Nota 1: ')))
    dadosps.append(float(input('Nota 2: ')))
    lista.append(dadosps[:])
    dadosps.clear()
    escolha = input('Deseja continuar?[S/N]: ')
    if escolha in 'Nn':
        break

count = 1
print()
print('=-'*30)
for p in lista:
    print(f'{count}    O aluno {p[0]} teve a média de: {(p[1] + p[2]) / 2}')
    count += 1
print('-'*60)

while True:
    count = int(input('deseja analisar a nota de algum aluno em especifico?[999 para cancelar]'))
    print()
    if count == 999:
        break
    else:
        print(f'O aluno {lista[count-1][0]} teve as respectivas notas: {lista[count-1][1]} e {lista[count-1][2]}')
        print()
        continue
print('-_-'*30)
print('Obrigado por usar meu programa')