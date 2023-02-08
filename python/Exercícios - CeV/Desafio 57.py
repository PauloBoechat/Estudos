sex = input('informe seu genero [M/F]: ').upper().strip()[0]

while sex not in 'MF':
    sex = input('Ops, parece que esse genero é invalido. Tente novamente [M/F]: ').upper().strip()[0]

print('Sexo {} registrado com sucesso'.format(sex))