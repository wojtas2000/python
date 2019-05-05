class BazaDanych:
    DOMYSLNA_NAZWA = "plik.txt"

    def __init__(self, nazwa_pliku):
        self.nazwa_pliku = nazwa_pliku

    @classmethod
    def init_with_default(cls):
        #return BazaDanych(cls.DOMYSLNA_NAZWA)
        return cls(cls.DOMYSLNA_NAZWA)


db1 = BazaDanych("plik2.txt")
db2 = BazaDanych.init_with_default()
