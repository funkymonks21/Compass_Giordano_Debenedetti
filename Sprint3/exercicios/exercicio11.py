import json

with open('person.json', 'r') as arquivo_json:
    dados = json.load(arquivo_json)
    print(dados)
