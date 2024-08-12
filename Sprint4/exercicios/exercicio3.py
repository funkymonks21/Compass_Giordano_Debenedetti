from functools import reduce


def calcula_saldo(lancamentos):
    valor_final = list(map(lambda n: n[0] if n[1] == 'C' else -n[0], lancamentos))
    valor_final = reduce(lambda a, b: a + b, valor_final)
    return float(valor_final)


if __name__ == '__main__':
    conteudo = [
    (200, 'D'),
    (300, 'C'),
    (100, 'C')
    ]
    print(f'Saldo = R$ {calcula_saldo(conteudo)}')
