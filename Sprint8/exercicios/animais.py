import csv

animais = ["cachorro", "gato", "rato", "elefante", "gorila",
           "tilapia", "formiga", "abelha", "leão", "girafa",
           "tartaruga", "águia", "jacaré", "toupeira", "coruja",
           "urso", "panda", "mosca", "mosquito", "beija-flor"]

animais.sort(reverse=False)

with open('animais_csv.csv',mode='w',newline='') as arquivo_csv:
    write_csv = csv.writer(arquivo_csv)
    for n in animais:
        print(f'{n}')
        write_csv.writerow([n])
