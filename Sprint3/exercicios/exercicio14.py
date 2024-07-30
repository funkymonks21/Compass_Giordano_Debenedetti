def funcao(*args, **kwargs):
    for arg in args:
        print(arg)
    for arg_nom in kwargs.values():
        print(f'{arg_nom}')


funcao(1, 3, 4, 'hello', parametro_nomeado='alguma coisa', x=20)
