def maior(t):
    vl = 0
    cont = 0
    for i in t:
        cont += 1
        if i > vl:
           vl = i
    print('-=' * 30)
    print('Analisando os valores passados...')
    for i in t:
        print(f'{i} ', end=' ')
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor digitado foi {vl}')
    print('-=' * 30)

maior((14,32,98,200,56,88,94,21))
maior((10,20,30,40,50))
maior((1,2,3,4,5,6,7,8,9))