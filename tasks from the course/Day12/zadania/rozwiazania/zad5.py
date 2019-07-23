# Dopisz do Czlowiek z zad5 możliwość zmiany wieku, jednak jeśli użytkownik poda wiek niższy niż aktualnie ustawiony
# rzuć wyjątek


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

    @wiek.setter
    def wiek(self, wartosc):
        if wartosc < self.__wiek:
            raise ValueError("Czlowiek nigdy nie mlodnieje")
        self.__wiek = wartosc
