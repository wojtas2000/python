class Klasa:
    def __init__(self):
        self.__prywatny_atrybut = 12
        self.atrybut2 = "publiczny"

    def daj_wartosc_prywatnego(self):
        return self.__prywatny_atrybut

    @property
    def atrybut(self):
        return self.__prywatny_atrybut

    @property
    def atrybut_zmienialny(self):
        return self.__prywatny_atrybut

    @atrybut_zmienialny.setter
    def atrybut_zmienialny(self, value):
        if value < 0:
            raise ValueError
        self.__prywatny_atrybut = value


instancja = Klasa()
# instancja.__prywatny_atrybut   # z zewnatrz nie ma dostepu
print(instancja.daj_wartosc_prywatnego())
print(instancja.atrybut)
print(instancja.atrybut2)
instancja.atrybut2 = "zmieniony"
print(instancja.atrybut2)
instancja.atrybut_zmienialny = 100
print(instancja.atrybut_zmienialny)
