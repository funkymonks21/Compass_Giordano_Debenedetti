def divide_lista(lista):
    tamanho_lista = len(lista)
    terco = tamanho_lista // 3
    lista_1 = lista[:terco]
    lista_2 = lista[terco:terco*2]
    lista_3 = lista[terco*2:]
    print(f'{lista_1} {lista_2} {lista_3}\n')


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
divide_lista(lista)
