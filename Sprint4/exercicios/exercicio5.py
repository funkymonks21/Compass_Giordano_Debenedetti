with open('estudantes.csv', 'r') as csv:
    linha = csv.readlines()

estudantes = []

for lin in linha:
    lin = lin.strip()
    campo = lin.split(',')
    nome = campo[0]
    notas = list(map(int, campo[1:]))
    estudantes.append((nome, notas))


def estudantes_proc(estudante):
    nome, notas = estudante
    top_notas = sorted(notas, reverse=True)[:3]
    media = round(sum(top_notas) / 3, 2)
    return nome, top_notas, media


proc = list(map(estudantes_proc, estudantes))

lista_estudante_ord = sorted(proc, key=lambda x: x[0])


def print_estudante(estudante):
    nome, top_notas, media = estudante
    return f"Nome: {nome} Notas: {top_notas} Média: {media:.2f}"


print("\n".join(map(print_estudante, lista_estudante_ord)))
