numeros = range(2, 100)
for x in numeros:
    if x == 2:
        print(x)
    elif x == 3:
        print(x)
    elif x == 5:
        print(x)
    elif x == 7:
        print(x)
    elif x % 2 != 0 and x % 3 != 0 and x % 5 != 0 and x % 7 != 0:
        print(x)
