print('-'*10,'Calculando Preço da Passagem','-'*10)
KM = int(input('Digite a distancia que será percorrida: '))
if KM>=200: print(f'A passagem custará {KM*0.5}')
else: print(f'A passagem custará {KM*0.45}')