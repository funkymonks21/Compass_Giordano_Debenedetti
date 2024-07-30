with open('arquivo_texto.txt', 'r') as arquivotxt:
    conteudo = arquivotxt.read()
    print(f'{conteudo}', end='')
