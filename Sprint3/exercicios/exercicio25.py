class Aviao:
    def __init__(self, modelo, velocidade_maxima, capacidade):
        self.modelo = modelo
        self.velocidade_maxima = velocidade_maxima
        self.capacidade = capacidade
        self.cor = "Azul"


aviao_1 = Aviao("BOIENG456", 1500, 400)
aviao_2 = Aviao("Praetor 600", 863, 14)
aviao_3 = Aviao("Antonov An-2", 258, 12)
avioes = [aviao_1, aviao_2, aviao_3]
for aviao in avioes:
    print(f'O avião de modelo {aviao.modelo} possuiu uma velocidade máxima de {
        aviao.velocidade_maxima} km/h, capacidade para {aviao.capacidade
                            } passageiros e é da cor {aviao.cor}.')
