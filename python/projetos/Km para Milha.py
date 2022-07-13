dt = fl = False
tb = True

while tb == True:

    while True:
        KoM = int(input('KM para Milha ou Milha para KM [1/2]: '))
        if KoM == 1:
            Km = float(input('digite o valor em KM: '))
            break
        elif KoM == 2:
            Mi = float(input('Digite o valor em Milha: '))
            break
        else:
            print('Algo deu errado, tente novamente')
    if KoM == 1:
        print('{}Km em Milhas fica {:.2f}'.format(Km, Km / 1.609))     
    else:
        print('{}Milhas em Km fica {:.2f}Km'.format(Mi, Mi*1.609))
        
    
    while True:
        ls = input('deseja sair?[S/N]: ').upper() .strip() [0]
        if ls != 'S' and ls != 'N':
            print('Isso não é uma opção valida, tente novamente: ')
        else:
            break
    if ls == 'S':
        break
            
