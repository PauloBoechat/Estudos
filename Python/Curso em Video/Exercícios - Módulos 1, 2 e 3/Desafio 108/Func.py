def aumentar(num, som=10):
    return [(num + (num * (som / 100))), som]

def diminuir(num, dim=10):
    return [num - (num * (dim / 100)), dim]

def dobro(num):
    return num * 2

def metade(num):
    return num / 2

def moeda(num, moeda='R$'):
    return f'{moeda}{num:.2f}'.replace('.', ',')