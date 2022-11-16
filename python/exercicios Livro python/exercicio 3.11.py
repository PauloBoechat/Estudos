valor = float(input('Digite o valor da mercadoria: '))
desconto = int(input('Digite o valor do desconto: '))

print(f'O produto com o valor de R${valor} receberá um desconto de R${valor * (desconto/100)} e ficará com o preço de {valor - (valor * (desconto/100))}')