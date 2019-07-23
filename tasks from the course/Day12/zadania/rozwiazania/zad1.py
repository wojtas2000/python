# uzyj klas Jacht, Pojazd i Samochod z zad1 z poprzednich zajęc.
# Do klasy Jacht dopisz metodę "po_czym_sie_poruszam" zwracajaca "Woda"
# Do klasy Samochod dopisz metodę "po_czym_sie_poruszam" zwracajaca "Asfalst"
# Stworz klase Ambfimbia dziedzicaca z Samochodu i z Jachtu
# Stworz instancje klasy Ambfimbia i dzialania metody "po_czym_sie_poruszam" na tej instancji
# Ktora metoda zostala wywolana?


class Pojazd:
    pass


class Samochod(Pojazd):
    def po_czym_sie_poruszam(self):
        return "asfalt"


class Jacht(Pojazd):
    def po_czym_sie_poruszam(self):
        return "woda"


class Amfibia(Jacht, Samochod):
    pass


a = Amfibia()
print(a.po_czym_sie_poruszam())
