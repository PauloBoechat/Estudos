conf = True
while True:
    print('(------------CONVERSOR DE TEMPERATURA------------)')
    print('OBS: ao usar numeros quebrados use "." ao inves de ",".')
    print()

    # Definindo variaveis
    S = N = False
    C = F = K = 0

    # Iniciando o programa
    while S == False:
        # Escolhendo a unidade de temperatura
        slk = input('selecione a unidade de temperatura (C/F/K):').upper() .strip() [0]

        if slk == 'C':
            C = float(input('Digite o valor em °C: '))
            S = True

        elif slk == 'F':
            F = float(input('Digite o valor em °F: '))
            S = True

        elif slk == 'K':
            K = float(input('Digite o valor em K:'))
            S = True

        # Caso seja digitado algo errado, tente novamente
        else:
            print()
            print('algo deu errado, tente novamente.')

        # Verifica se o número é menor que 0 ou seja negativo
        if C < 0:
            N == True
        if F < 0:
            N == True
        if N == True:
            CF = (-C * 9/5) + 32
            CK = -C + 273.15
            FC = (-F - 32) * 5/9
            FK = (-F - 32) * 5/9 + 273.15
        else:
            CF = (C * 9/5) + 32
            CK = C + 273.15
            FC = (F - 32) * 5/9
            FK = (F - 32) * 5/9 + 273.15
            KC = K - 273.15
            KF = (K - 273.15) * 9/5 + 32


    # Verifica se o numero é diferente de 0
    if C != 0:
        print(f'{C}°C fica {CF:.2f}°F que fica {CK:.2f} K '.format(C, CF, CK))
    if F != 0:
        print(f'{F}°F fica {FC:.2f}°C que fica {FK:.2f} K '.format(F, FC, FK))
    if K != 0:
        print(f'{K} K fica {KC:.2f}°C que fica {KF:.2f}°F '.format(K, KC, KF))

    # Deseja continuar?
    l = input('Deseja sair?[S/N]: ').upper() .strip() [0]
    if l == 'N':
        print('')
        continue
    else:
        print('')
        break

print('Obrigado por usar o programa!')
