

def voto(nasc=2000):
    """
    :param nasc: ano de nascimento
    :return: Função eleitoral
    """
    from datetime import date
    idade = date.today().year - nasc
    if idade < 18 and idade >= 16:
        return f'Com {idade} anos: VOTO OPCIONAL'
    elif idade >= 18 and idade < 65:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'
    else:
        return f'Com {idade} anos: NÃO VOTA'

print('-=' * 30)

nasc = int(input('Digite seu ano de nascimento: '))

print(voto(nasc))

help(voto)