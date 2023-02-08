Dias = int(input('Digite a quantidade de dias: '))
Horas = int(input('Digite a quantidade de horas: '))
Minutos = int(input('Digite a quantidade de minutos: '))
Segundos = int(input('Digite a quantidade de segundos: '))

total = (((Horas + (Dias * 24)) + Minutos) * 60) + Segundos

print(total)