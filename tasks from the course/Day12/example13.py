class KlasaA:
    def __init__(self):
        self.__priv = 12

    def __prywatna_metoda(self):
        pass


class KlasaB(KlasaA):
    def wypisz(self):
        print(self.__priv)


b = KlasaB()
b.wypisz()
