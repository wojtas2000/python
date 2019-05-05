class Silnik:
    def __init__(self, moc):
        self.moc = moc


class Samochod:
    def __init__(self, marka, silnik):
        self.marka = marka
        self.silnik = silnik


silnik = Silnik(100)
print(silnik)
samochod = Samochod("Volvo", silnik)

silnik2 = Silnik(500)
print(silnik2)
samochod2 = Samochod('Porshe', silnik2)

print(samochod.silnik.moc)
print(samochod2.silnik.moc)

samochod3 = samochod   # NIE TWORZYMY NOWEGO OBIEKTU
# tylko przypisujemy referencje do nowej zmiennej
# zmienne samochod3 i samochod wskazuja na TA SAMA instancje klasy Samochod


