RED   = "\033[1;31m"  
GREEN = "\033[0;32m"
RESET = "\033[0;0m"


expressao = input('Digite a expressão que será testada: ')

abre_ex = expressao.count('(')
fecha_ex = expressao.count(')')

if abre_ex == fecha_ex:print(f'{GREEN}Essa expressão é compativel{RESET}')
else:print(f'{RED}Essa expressão não é compativel{RESET}')