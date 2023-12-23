import Func

num = int(input('Digite o preço: R$'))

print(f'A metade de {Func.moeda(num)} é {Func.moeda(Func.metade(num))}')

print(f'O dobro de {Func.moeda(num)} é {Func.moeda(Func.dobro(num))}')

print(f'Aumentando {Func.aumentar(num)[1]}%, temos {Func.moeda(Func.aumentar(num, 10)[0])}')

print(f'Diminuindo {Func.diminuir(num, 13)[1]}%, temos {Func.moeda(Func.diminuir(num, 13)[0])}')