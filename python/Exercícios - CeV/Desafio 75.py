v9 = p3 = pares = 0
num = int(input('Digite um valor: ')), int(input('Digite outro valor: ')), int(input('Digite mais um valor: ')), int(input('Digite o penultimo valor: ')), int(input('Digite o ultimo valor: '))

v9 = num.count(9)

for n in num:
    if n % 2 == 0:
        pares += 1
    if n == 3:
        p3 += 1


print(f'nessa tupla tem {v9} noves!')

if p3 >= 1:
    print(f'nessa tupla o três está na {num.index(3) + 1}° posição!')
else:
    print('Não tem nenhum três nessa tupla!')

print(f'Nessa tupla tem {pares} numeros pares!')