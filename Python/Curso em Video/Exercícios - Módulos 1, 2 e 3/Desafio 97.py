def Bprint(TXT):
    print('-'*30)
    print('\033[1m',TXT,'\033[0m')
    print('-' * 30)

txt = str(input('Digite o que será printado: ')).upper()
Bprint(txt)