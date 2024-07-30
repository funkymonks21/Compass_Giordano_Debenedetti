import random

random_list = random.sample(range(500), 50)

lista_org = sorted(random_list)
met = len(lista_org) // 2


mediana = ((lista_org[met - 1] + (lista_org[met])) / 2)
media = sum(random_list) / len(random_list)
valor_minimo = min(random_list)
valor_maximo = max(random_list)

print(f'Media: {media}, Mediana: {mediana}, \
      Mínimo: {valor_minimo}, Máximo: {valor_maximo}')
