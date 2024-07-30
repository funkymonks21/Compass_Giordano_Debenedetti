def tira_virgula(string):
    numero = string.split(',')
    soma = sum(int(num) for num in numero)
    return soma


string = "1,3,4,6,10,76"
print(tira_virgula(string))
