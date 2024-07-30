with open("actors.csv", 'r') as arquivo:
    linhas = arquivo.readlines()

cabecalho = linhas[0].strip().split(',')
dados = linhas[1:]

cont_filme = {}

for linha in dados:
    temp = linha.strip().split(',')
    filme_1 = temp[4]

    if filme_1 in cont_filme:
        cont_filme[filme_1] += 1
    else:
        cont_filme[filme_1] = 1

lista_desc = sorted(cont_filme.items(), key=lambda x: (-x[1], x[0]))

with open('etapa_4.txt', 'w') as output:
    for index, (filme, cont) in enumerate(lista_desc, start=1):
        output.write(f'{index} - O filme {filme} aparece {cont} vez(es)\
no dataset.\n')
