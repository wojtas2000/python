# Uzyj klas z zad1
# Dopisz do klasy Pojazd metode stoj() wypisujaca na ekran "Przeciez stoje"
# Dopisz do klasy Jacht metode plyn() wypisujaca na ekran "Przez morza i oceany!"
# Dopisz do klasy Samochod metode jedz() wypisujaca na erkan "W strone slonca1"

# Wywolaj metode plyn() na instancjach klas JachtMotorowy i JachtZaglowy
# Wywolaj metode stoj() na kazdej z instancji


class Pojazd:
    def stoj(self):
        print("Przeca stoje")


class Samochod(Pojazd):
    def jedz(self):
        print("W strone slonca")


class Jacht(Pojazd):
    def plyn(self):
        print("Przez morza i oceany")


class JachtMotorowy(Jacht):
    pass


class JachtZaglowy(Jacht):
    pass


samochodzik = Samochod()
samochodzik.jedz()
samochodzik.stoj()

zagloweczka = JachtZaglowy()
zagloweczka.plyn()
zagloweczka.stoj()

motoroweczka = JachtMotorowy()
motoroweczka.plyn()
motoroweczka.stoj()
