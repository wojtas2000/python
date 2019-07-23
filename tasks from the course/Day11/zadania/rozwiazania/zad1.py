# napisz klasy:
# Pojazd
# Jacht dziedziczacy z Pojazd
# Samochod dziedziczacy z Pojazd
# JachtZaglowy dziedzicacy z Jacht
# JachtMotorowy dziedzicacy z Jacht
#
# Stworz po jednej instancji kazdej klasy
# Sprawdz czy:
# - instancja Samochod to Pojazd
# - instancja Samochod to Jacht
# - instancja JachtMotorowy to Jacht
# - instancja JachtZaglowy to Pojazd


class Pojazd:
    pass


class Samochod(Pojazd):
    pass


class Jacht(Pojazd):
    pass


class JachtMotorowy(Jacht):
    pass


class JachtZaglowy(Jacht):
    pass


pojazd = Pojazd()
samochodzik = Samochod()
jachcik = Jacht()
zagloweczka = JachtZaglowy()
motoroweczka = JachtMotorowy()

print("Czy samochodzik to Pojazd?", isinstance(samochodzik, Pojazd))
print("Czy samochodzik to Jacht?", isinstance(samochodzik, Jacht))
print("Czy motoroweczka to Jacht?", isinstance(motoroweczka, Jacht))
print("Czy zagloweczka to Pojazd?", isinstance(zagloweczka, Pojazd))
