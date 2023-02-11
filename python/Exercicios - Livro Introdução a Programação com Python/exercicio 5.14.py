x = 0
ac = 0
while True:
    N = int(input('Digite um número(0 para parar): '))
    if N == 0:
        break
    print(N)
    ac += N
    x += 1

print(f'Você digitou {x} números e a soma entre eles é {ac} e a média entre eles é {ac / x:.2f}')