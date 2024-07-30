class Passaro:
    def voar(self):
        print("Voando...")

    def emitir_som(self):
        pass


class Pato(Passaro):
    def emitir_som(self):
        print("Quack Quack")


class Pardal(Passaro):
    def emitir_som(self):
        print("Piu Piu")


def testar_passaros():
    pato = Pato()
    pardal = Pardal()

    print("Pato")
    pato.voar()
    print("Pato emitindo som...")
    pato.emitir_som()

    print("Pardal")
    pardal.voar()
    print("Pardal emitindo som...")
    pardal.emitir_som()


testar_passaros()
