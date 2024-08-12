def maiores_que_media(conteudo):
    media = sum(conteudo.values()) / len(conteudo)
    acima_da_media = [(produto, preco) for produto, preco in conteudo.items() if preco > media]
    acima_da_media.sort(key=lambda x: x[1])
    return acima_da_media


conteudo = {
    "arroz": 4.99,
    "feijão": 3.49,
    "macarrão": 2.99,
    "leite": 3.29,
    "pão": 1.99
}

if __name__ == '__main__':
    print(f'Produtos acima da media: {maiores_que_media(conteudo)}')
