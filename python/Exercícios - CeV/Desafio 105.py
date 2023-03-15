def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma
    """
    f = dict()
    f['total'] = len(n)
    f['maior'] = max(n)
    f['menor'] = min(n)
    f['média'] = sum(n)/len(n)
    if sit and f['média'] >= 7: f['situação'] = 'Bom'
    elif sit and f['média'] < 6: f['situação'] = 'Ruim'
    elif sit and f['média'] == 5: f['situação'] = 'Razoavel'
    return f

rsp = notas(10,8,9.4, sit=True)
print(rsp)
