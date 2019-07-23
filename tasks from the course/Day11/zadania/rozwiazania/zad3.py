# uzywaj klas z Zad2
# dopisz do klasy Jacht konstruktor przyjmujacy dlugosc_jachtu i ustawiajacy jako atrybut
# dopisz do klasy Jacht metode max_predkosc() wypisujaca na ekran wynik:
# 2,42 x pierwiastek(dlugosc_jachtu)
# dopisz do klasy JachtMotorowy metode max_predkosc() wypisujaca "ile fabryka dała!"
# wykonaj metody max_predkosc na instancji JachtZaglowy i JachtMotorowy
import math


class Pojazd:
    def stoj(self):
        print("Przeca stoje")


class Jacht(Pojazd):
    def __init__(self, dlugosc_jachtu):
        self.dlugosc_jachtu = dlugosc_jachtu

    def plyn(self):
        print("Przez morza i oceany")

    def max_predkosc(self):
        print("{} węzłów".format(
            2.42 * math.sqrt(self.dlugosc_jachtu)
        ))


class JachtMotorowy(Jacht):
    def max_predkosc(self):
        print("Ile fabryka dała!")


class JachtZaglowy(Jacht):
    pass


zagloweczka = JachtZaglowy(5.5)
motorowka = JachtMotorowy(7)

zagloweczka.max_predkosc()
motorowka.max_predkosc()
