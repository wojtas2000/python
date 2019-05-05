class Klasa:
    zmienna_klasowa = 12

    def wypisz_zmienna(self):
        print(self.zmienna_klasowa)


a = Klasa()
a.wypisz_zmienna()
b = Klasa()
b.wypisz_zmienna()

Klasa.zmienna_klasowa = 4
a.wypisz_zmienna()
# print(Klasa.zmienna_klasowa)


