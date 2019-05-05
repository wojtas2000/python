class LadnieWypiszMixin(object):
    def ladnie_wypisz(self):
        print("==============")
        print(self)
        print("==============")


class Pojazd:
    pass


class Samochod(Pojazd, LadnieWypiszMixin):
    pass


class Zwierze:
    pass


class Kot(Zwierze, LadnieWypiszMixin):
    pass


kicia = Kot()
kicia.ladnie_wypisz()
autko = Samochod()
autko.ladnie_wypisz()
