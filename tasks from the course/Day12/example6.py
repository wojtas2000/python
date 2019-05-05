class Klasa:
    zmienna_klasowa = 12

    def wypisz_zmienna(self):
        print(self.zmienna_klasowa)

    def zmien_zmienna(self):
        # w ten sposob tworzymy nowa zmienna na instancji
        self.zmienna_klasowa = 4

        # w ten sposob zmienimy wartosc zmiennej klasowej
        Klasa.zmienna_klasowa = 5


print(Klasa.zmienna_klasowa)
a = Klasa()
b = Klasa()
a.zmien_zmienna()
b.wypisz_zmienna()
a.wypisz_zmienna()
print(Klasa.zmienna_klasowa)
