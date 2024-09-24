import requests
import json

# Essa url é para obter todos os filmes que o Steven Spielberg participou
# Vou separar depois pelos filmes que ele dirigiu de ficcao científica
steven_url = "https://api.themoviedb.org/3/person/488/movie_credits"

# Informo o meu token para o request
headers = {
    "accept": "application/json",
    "Authorization": "Bearer MEU TOKEN DE ACESSO"
}

# Aqui eu obtenho a resposta, se for "200", significa que a minha requisição deu certo, assim eu gravo os dados localmente.
# Caso tenha dado errado, me retorna o erro.
response = requests.get(steven_url, headers=headers)

if response.status_code == 200:
    dados_steven = response.json()

    # Aqui eu estou filtrando apenas pelos filmes que o Steven dirigiu
    # São de ficção científica e foram lançados até 2022, ano máximo do CSV dos dados do IMDB
    filmes_dirigidos = [movie['id'] for movie in dados_steven['crew']
                        if movie['job'] == 'Director' 
                        and 878 in movie['genre_ids']
                        and movie['release_date'] and int(movie['release_date'][:4]) < 2023]

    # Vou criar uma lista com os detalhes dos filmes filtrados
    filmes_sci_fi = []

    for id_filme in filmes_dirigidos:
        # Aqui o código cria uma url para cada filme, afim de obter mais detalhes que serão analisados
        filme_url = f"https://api.themoviedb.org/3/movie/{id_filme}"
        response_filme = requests.get(filme_url, headers=headers)

        if response_filme.status_code == 200:
            dados_filmes = response_filme.json()

            # Vou filtrar os dados que eu vou usar para a minha análise.
            filmes_filtrados = {
                "id": dados_filmes['id'],
                "imdb_id": dados_filmes['imdb_id'],
                "title": dados_filmes['title'],
                "release_date": dados_filmes['release_date'],
                "genres": dados_filmes['genres'],
                "budget": dados_filmes['budget'],
                "revenue": dados_filmes['revenue'],
                "vote_average": dados_filmes['vote_average'],
                "vote_count": dados_filmes['vote_count'],
                "popularity": dados_filmes['popularity']
            }
            filmes_sci_fi.append(filmes_filtrados)
        else:
            print(f'Erro ao obter detalhes do filme de id {id_filme} - Erro {response_filme.status_code}')

    with open('filmes-sci-fi-steven.json', 'w') as arquivo:
        json.dump(filmes_sci_fi, arquivo, indent=4)

else:
    print(f"Erro {response.status_code}")
