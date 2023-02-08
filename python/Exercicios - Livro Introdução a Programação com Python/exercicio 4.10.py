TP = str(input('Qual é o tipo de instalação("R"esidencial, "C"omercial ou "I"ndustrial): '))
KWH = float(input('Digite a quantidade de KWh: '))

if TP == "R":
   if KWH >= 500: print(f'O preço da conta ficará: R${KWH * 0.40}')
   else: print(f'O preço da conta ficará: R${KWH * 0.65}')

elif TP == "C":
    if KWH >= 1000: print(f'O preço ficará: R${KWH * 0.55}')
    else: print(f'O preço ficará: R${KWH * 0.6}')
    
elif TP == "I":
    if KWH >= 5000: print(f'O preço ficará: R${KWH * 0.55}')
    else: print(f'O preço ficará: R${KWH * 0.6}')

else: print('Essa opção é invalida! Tente novamente.')