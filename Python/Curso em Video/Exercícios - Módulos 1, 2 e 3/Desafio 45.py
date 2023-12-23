from random import randint


print('pedra: 1, tesoura: 2, papel: 3')
sus = int(input('escolha a sua arma'))
enm = randint(1, 3)

if sus == 1 and enm == 2:
    print('parabéns você ganhou')

elif sus == 2 and enm == 3:
    print('parabéns você ganhou')

elif sus == 1 and enm == 3:
    print('parece que você perdeu')

elif sus == 2 and enm == 1:
    print('parece que você perdeu')

elif sus == 3 and enm == 3:
    print('parece que você perdeu')

elif sus == 3 and enm == 2:
    print('parabéns você ganhou')



elif sus == enm:
    print('empate')