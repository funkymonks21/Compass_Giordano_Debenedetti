with open("actors.csv", 'r') as arquivo:
    linhas = arquivo.readlines()

cabecalho = linhas[0].strip().split(',')
dados = [linha.strip().split(',') for linha in linhas[1:]]
index_num_filmes = cabecalho.index("Number of Movies")
mais_filmes = 0
ator_mais_filmes = ""

for col in dados:
    ator = col[0]
    num_filmes = int(col[index_num_filmes])

    if num_filmes > mais_filmes:
        mais_filmes = num_filmes
        ator_mais_filmes = ator

print_arquivo = f'{ator_mais_filmes} é o ator com mais filmes,' \
 f'tendo feito {mais_filmes} filmes.'

with open("etapa_1.txt", 'w') as output:
    output.write(print_arquivo)
