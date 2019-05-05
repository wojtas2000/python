class Klasa:
    def __init__(self):
        self.__prywatny_atrybut = 12

    def wypisz_prywatny(self):
        print(self.__prywatny_atrybut)


a = Klasa()
a.wypisz_prywatny()
# print(a.__prywatny_atrybut)  # ten kod rzuci blad!
