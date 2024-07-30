def my_map(list, f):
    nova_lista = []
    for num in list:
        nova_lista.append(f(num))
    return nova_lista


def potencia(lista):
    return lista ** 2


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(my_map(lista, potencia))
