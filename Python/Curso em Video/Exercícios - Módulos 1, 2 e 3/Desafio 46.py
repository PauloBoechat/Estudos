from time import sleep

n = int(input('digite em segundos o tempo que falta para o ano novo: '))

for c in range(n, 0, -1):
    print(c)
    sleep(1)

print('FELIZ ANO NOVO!!!!!')