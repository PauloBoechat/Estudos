s = 0
while True:
    n = int(input('digite um número(999 para parar): '))
    if n == 999:
        break
    else:
        s += n
print(f'A adição de todos os números dá {s}')