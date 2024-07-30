with open("actors.csv", 'r') as arquivo:
    linhas = arquivo.readlines()

cabecalho = linhas[0].strip().split(',')
dados = [linha.strip().split(',') for linha in linhas[1:]]

gross = [float(col[5]) for col in dados]
media_gross = sum(gross) / len(gross)

with open("etapa_2.txt", 'w') as output:
    output.write(f'A média de receita bruta é {media_gross} \
milhões de dolares.')
