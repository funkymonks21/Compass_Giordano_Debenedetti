def limpa_lista(lista):
    return list(set(lista))


lista = ['abc', 'abc', 'abc', '123', 'abc', '123', '123']
print(limpa_lista(lista))
