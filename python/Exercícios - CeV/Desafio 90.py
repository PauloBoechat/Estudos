geral = dict()
geral['Nome'] = str(input('Aluno: '))
geral['Média'] = float(input('Média: '))

print(f'O nome do aluno é {geral["Nome"]}')
print(f'A média do aluno é {geral["Média"]}')

if geral['Média'] < 7:
    print('O aluno está \033[1;31mreprovado\033[0;0m')

else:
    print('O aluno está \033[1;32maprovado\033[0;0m')
    
