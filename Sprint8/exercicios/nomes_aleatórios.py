import names
import random

random.seed(40)

qtd_nomes_unicos = 3000

qtd_nomes_aleatorios = 10000000

lista_nomes_unicos = []

for i in range(0, qtd_nomes_unicos):
    lista_nomes_unicos.append(names.get_full_name())

print(f'Gerando {qtd_nomes_aleatorios} nomes aleatórios.')

lista_nomes_aleatorios = []

for i in range(0, qtd_nomes_aleatorios):
    lista_nomes_aleatorios.append(random.choice(lista_nomes_unicos))

with open('nomes_aleatorios.txt','w') as arquivo_txt:
    for nome in lista_nomes_aleatorios:
        arquivo_txt.write(nome + "\n")

