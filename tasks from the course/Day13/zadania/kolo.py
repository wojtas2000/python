class Kolo(object):
    def __init__(self, promien):
        if not isinstance(promien, (int, float)):
            raise ValueError("Zly typ!")
        if promien <= 0:
            raise ValueError("Promien musi byc wiekszy od 0!")
        self.__promien = promien

    @property
    def promien(self):
        return self.__promien

    @promien.setter
    def promien(self, wartosc):
        if wartosc <= 0:
            raise ValueError("Promien musi byc wiekszy od 0!")
        self.__promien = wartosc

    @property
    def srednica(self):
        return self.__promien * 2

    @srednica.setter
    def srednica(self, value):
        if value <= 0:
            raise ValueError("Srednica musi byc wieksza od 0!")
        self.__promien = value / 2


kolo = Kolo(12)
print("Promien", kolo.promien)
print("Srednica", kolo.srednica)

kolo.promien = 10
print("Promien", kolo.promien)
print("Srednica", kolo.srednica)

kolo.srednica = 14
print("Promien", kolo.promien)
print("Srednica", kolo.srednica)

