with open("actors.csv", 'r') as arquivo:
    linhas = arquivo.readlines()

cabecalho = linhas[0].strip().split(',')
dados = linhas[1:]

maior_media = 0.0
ator_melhor_media = ""

for lin in dados:
    temp = lin.strip().split(',')
    ator = temp[0]
    media = float(temp[3])

    if media > maior_media:
        maior_media = media
        ator_melhor_media = ator

print_arquivo = f'O ator {ator_melhor_media} tem a maior media \
de receita, com {maior_media} milhões de dolares de media.'

with open('etapa_3.txt', 'w') as output:
    output.write(print_arquivo)
