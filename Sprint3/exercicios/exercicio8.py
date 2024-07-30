a = ['maça', 'arara', 'audio', 'radio', 'radar', 'moto']
b = [x[::-1] for x in a]
for x in range(len(a)):
    if a[x] == b[x]:
        print('A palavra:', a[x], 'é um palíndromo')
    else:
        print('A palavra:', a[x], 'não é um palíndromo')
