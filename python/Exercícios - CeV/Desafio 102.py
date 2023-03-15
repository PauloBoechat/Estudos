def fatorial(n, show=False):
    """
    -> Calcula o fatorial de um número n.
    :param n: O número a ser calculado.
    :param show: Mostrar ou não a conta.
    :return: O fatorial de n."""
    f = 1
    for c in range(n, 0, -1):
        f *= c
        if show:
            print(c,end='')
            if c>1: print(' x ', end='')
            else: print(' = ', end='')
    return f

print(fatorial(5, True))