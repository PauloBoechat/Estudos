VC = float(input('Digite o valor da casa: R$'))
SL = float(input('Digite o valor do salario: R$'))
QA = int(input('Digite a quantidade de anos a pagar: '))

prest = VC / (QA * 12)

if prest <= SL * 0.3: print('Infelizmente não será liberado o impréstimo.')
else: print('Parabéns, seu imprestimo foi autorizado!')