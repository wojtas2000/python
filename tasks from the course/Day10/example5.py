# ten plik pokazuje zle praktyki, na nim sie nie wzorowac!
class Samochod:
    def __init__(self):
        # dobra praktyka jest w konstruktorze definiować
        # wszystkie atrybuty ktore ma miec instancja klasy
        self.atrybut = None

    def przypisz_kolor(self, kolor):
        self.kolor = kolor
        # to rowniez jest zla praktyka


samochod = Samochod()
samochod.marka = "Volvo"  # to jest zla praktyka

print(samochod.marka)
