class Samochod:
    def __init__(self, marka):
        self.marka = marka


napis = "Volvo"
samochod = Samochod(napis)
napis = "Audi"
print(samochod.marka)
