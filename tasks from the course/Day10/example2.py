class Samochod:
    def __init__(self, marka):
        self.marka = marka
        self.predkosc = 0

    def przyspiesz(self, wartosc):
        print(self)
        self.predkosc += wartosc


samochod = Samochod("Volvo")  # tworzymy instancje klasy Samochod
print(samochod)
print(samochod.marka)
print(samochod.predkosc)
samochod.przyspiesz(12)
print(samochod.predkosc)
samochod.przyspiesz(5)
print(samochod.predkosc)
