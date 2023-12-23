# Programa 9.1 - Abrindo, Lendo e Fechando o Arquivo
arquivo = open("Números.txt", "w")
for linha in range(1 ,101):
    arquivo.write(f"{linha}\n")
arquivo.close()

arquivo = open("Números.txt", "r")
for linha in arquivo.readlines():
    print(linha)
arquivo.close()
