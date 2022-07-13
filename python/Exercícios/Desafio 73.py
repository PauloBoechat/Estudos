times = 'Bragantino', 'Atlético-MG', 'Santos', 'Cuiabá', 'Corinthians', 'América-MG', 'Internacional', 'Avaí', 'Palmeiras', 'Flamengo', 'Botafogo', 'Coritiba', 'São Paulo', 'Fluminese', 'Ceará SC', 'Athletico-PR', 'Atlético-GO', 'Goiás', 'Juventude', 'Fortaleza'


print('-'*20)
print('A) Apenas os 5 primeiros times')
print('B) Os ultimos 4 colocados da tabela')
print('C) Lista de times em hordem alfabética')
print('D) Posição do Flamengo na tabela')
print('-'*20)

while True:
    teams = input('Digite a opção que deseja: ').strip() .upper()
    if teams in 'ABCD':
        break
    else:
        print('algo deu errado, tente novamente!')
        continue

if teams == 'A':
    print(times[0:6])

elif teams == 'B':
    print(times[20 - 4:20])

elif teams == 'C':
    print(sorted(times))

else:
    print('A posição do Flamendo é como 10° colocado')