def contagem(de,até,pas):
    print(f'Contagem de {de} até {até} de {pas} em {pas}')
    if de <= até:
        for val in range(de,até + 1,pas):
            print(val,end=' ')
        print()
    elif de >= até:
        for val in range(de,até - 1,-pas):
            print(val,end=' ')
        print()

def linha(val):
    print(str(val)*30)


linha('-')
contagem(0,10,1)
linha('-')
print()

linha('-')
contagem(10,0,1)
linha('-')
print()

linha('~')
de = int(input('digite o valor inicial: '))
até = int(input('digite o valor final : '))
pas = int(input('digite o valor que será pulado(de casa em casa): '))
contagem(de,até,pas)
linha('~')

print(f'Obrigado por usar o programa! :)')