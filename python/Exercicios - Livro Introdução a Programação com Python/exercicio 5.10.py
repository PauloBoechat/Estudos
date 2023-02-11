pontos = 0
quest = 1
while quest <=3:
    resp = input(f'Resposta da questão {quest}: ').upper()
    if quest == 1 and resp == "B":
        pontos += 1
    if quest == 2 and resp == "A":
        pontos += 1
    if quest == 3 and resp == "D":
        pontos += 1
    quest += 1
print(f'Você acertou com {pontos} pontos!')