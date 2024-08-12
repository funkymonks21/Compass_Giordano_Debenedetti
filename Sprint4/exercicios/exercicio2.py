def conta_vogais(texto):
    vogal = filter(lambda x: x in 'aeiouAEIOU', texto)
    return len(list(vogal))


if __name__ == '__main__':
    texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque\
    eu posuere arcu. Fusce fermentum sodales massa eget hendrerit. Morbi\
          sagittis nibh magna, sit amet facilisis"
    cont_vogais = conta_vogais(texto)
    print(f'A frase tem {cont_vogais} vogais.')
