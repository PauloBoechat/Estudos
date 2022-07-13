from time import strftime

dados = dict()
dados['nome'] = str(input('Nome: '))
dados['idade'] = int(strftime("%Y")) - int(input('Ano de nascimento: ')) 
dados['CTPS'] = int(input('Digite a carteira de trabalho (0 se não houver): '))

if dados['CTPS'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salário'] = float(input('salário: R$'))

for k, i in dados.items():
    print(f'  - {k} tem o valor {i}')

