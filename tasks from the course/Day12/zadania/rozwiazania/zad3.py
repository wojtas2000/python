# Stworz klase "Geometria" ze statycznymi metodami:
# - Pole koła o zadanym promieniu
# - Pole kwadratu o podanym boku
# Wywolaj dane metody BEZ tworzenia instancji klasy

class Geometria:
    PI = 3.14

    @staticmethod
    def pole_kola(r):
        return Geometria.PI * (r**2)

    @staticmethod
    def pole_kwadrat(a):
        return a**2


print(Geometria.pole_kola(100))
print(Geometria.pole_kwadrat(10))
