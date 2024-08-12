def ordena(par):
    return sorted(list(par), reverse=True)[:5]


numeros = open('number.txt', 'r')

numeros = list(map(int, numeros))

pares = list(filter(lambda n: n % 2 == 0, numeros))

maiores_pares = ordena(pares)

soma = sum(maiores_pares)

print(f'{maiores_pares}\n{soma}')
