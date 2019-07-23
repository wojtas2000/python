# Napisz klase czlowiek posiadajaca atrybuty imie i wiek
# Atrybuty powinny być niemożliwe to (prostego) zmienienia z zewnątrz


class Czlowiek:
    def __init__(self, imie, wiek):
        self.__imie = imie
        self.__wiek = wiek

    @property
    def imie(self):
        return self.__imie

    @property
    def wiek(self):
        return self.__wiek


bartek = Czlowiek("Bartek", 29)
print(bartek.imie)
bartek.imie = "Wojtek"