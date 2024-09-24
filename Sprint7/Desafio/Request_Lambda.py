import json
import requests
import boto3
from datetime import datetime
import os

s3 = boto3.client('s3')

# Guardei meu token de acesso da API em uma variável de ambiente, por questões de segurança.
# Utilizo o módulo 'os' para pegar conteúdo da variável.
API_TOKEN = os.environ['API_TOKEN']

# URL para procurar os filmes que o Steven Spielberg participou
# Depois vou filtrar por filmes de ficção científica que ele dirigiu
steven_url = "https://api.themoviedb.org/3/person/488/movie_credits"


headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {API_TOKEN}"
}

# Função padrão do lambda. Essa função vai fazer os requests, pegar os dados, extrair apenas o que eu quero e salvar no Data Lake em formato JSON.
def lambda_handler(event, context):
    response = requests.get(steven_url, headers=headers)

    if response.status_code == 200:
        # Caso o retorno seja positivo, ou seja, código 200, o código salva todo o conteúdo em uma variável com "formato" json
        dados_steven = response.json()

        # Aqui eu estou filtrando os dados obtidos anteriormente
        # Estou apenas salvando as 'ids" dos filmes de ficção científica que o Steven Spielberg dirigiu.
        filmes_dirigidos = [
            movie['id'] for movie in dados_steven['crew'] 
            if movie['job'] == 'Director' 
            and 878 in movie['genre_ids'] 
            and movie['release_date'] and int(movie['release_date'][:4]) < 2023
        ]

        # Crio uma lista vazia, aqui vou guardar os dados que quero.
        filmes_sci_fi = []

        # Percorro todos os filmes obtidos, faço um request para obter os detalhes dos filmes.
        for id_filme in filmes_dirigidos:
            filme_url = f"https://api.themoviedb.org/3/movie/{id_filme}"
            response_filme = requests.get(filme_url, headers=headers)

            # Caso seja o retorno seja positivo, salvo apenas os dados que quero para a minha análise.
            if response_filme.status_code == 200:
                dados_filmes = response_filme.json()

                filmes_filtrados = {
                    "id": dados_filmes['id'],
                    "imdb_id": dados_filmes["imdb_id"],
                    "title": dados_filmes['title'],
                    "release_date": dados_filmes['release_date'],
                    "genres": dados_filmes['genres'],
                    "budget": dados_filmes['budget'],
                    "revenue": dados_filmes['revenue'],
                    "vote_average": dados_filmes['vote_average'],
                    "vote_count": dados_filmes['vote_count'],
                    "popularity": dados_filmes['popularity']
                }

                # Adiciono os dados para a lista vazia criada anteriormente
                filmes_sci_fi.append(filmes_filtrados)
                
            # Caso ocorra um erro com a requisição do filme, printa o erro.
            else:
                print(f'Erro ao obter detalhes do filme de id {id_filme} - ERRO {response_filme.status_code}')

        # Aqui eu estou colocando os dados obtidos no formato JSON
        json_data = json.dumps(filmes_sci_fi, indent=4)

        # O módulo datetime extrai o ano, mês e dia do meu sistema. Vou usar esses dados para criar os subdiretórios do bucket
        data_hoje = datetime.now()
        ano = data_hoje.year
        mes = data_hoje.month
        dia = data_hoje.day

        # Por fim eu crio a variável com o nome do arquivo que vai ser salvo, também crio o caminho de diretórios do meu bucket e informo o nome do bucket
        nome_arquivo = "filmes-sci-fi-steven.json"
        caminho_s3 = f"Raw/TMDB/JSON/{ano}/{mes}/{dia}/{nome_arquivo}"
        nome_bucket = 'data-lake-giordano'

        # Esse bloco de comandos salva o arquivo JSON para dentro do caminho especificado dentro do bucket.
        try:
            s3.put_object(
                Bucket=nome_bucket,
                Key=caminho_s3,
                Body=json_data,
                ContentType='application/json'
            )
            print(f"Arquivo carregado com sucesso")

        # Caso ocorra um erro no carregamento do arquivo, printa o erro
        except Exception as e:
            print(f"Erro ao carregar o arquivo - ERRO {e}")

    # Caso ocorra um erro na requisição, printa o erro.
    else:
        print(f"Erro na requisição - ERRO {response.status_code}")