with open("actors.csv", 'r') as arquivo:
    linhas = arquivo.readlines()

cabecalho = linhas[0].strip().split(',')
dados = linhas[1:]

atores = []

for lin in dados:
    temp = lin.strip().split(',')
    ator = temp[0]
    receita_total = float(temp[1])
    atores.append((ator, receita_total))

ator_desc = sorted(atores, key=lambda x: -x[1])

with open('etapa_5.txt', 'w') as output:
    for ator, receita_total in ator_desc:
        output.write(f'{ator} - {receita_total}\n')
