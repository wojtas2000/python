# stworzmy klase Flota posiadajaca atrybut 'jachty' bedacy poczatkowo pusta lista
# dajmy klasie Flota metode
# dodaj_jacht dodjacy do listy "jachty" instancje klasy Jacht (z zad 4)

import zad4

class Flota:
    def __init__(self):
        self.jachty = []

    def dodaj_jacht(self, jacht):
        self.jachty.append(jacht)


piraci = Flota()
czarna_perla = zad4.Jacht("Czarna Perla", zad4.Zagiel(100, "Pajęczyny"))
flying_dutch = zad4.Jacht("Latający Holender", zad4.Zagiel(150, "Rybie błony"))

piraci.dodaj_jacht(czarna_perla)
piraci.dodaj_jacht(flying_dutch)

print(piraci.jachty)
print("Flota piracka sklada się z takich jachtów: ")
for jacht in piraci.jachty:
    print(jacht.nazwa)
