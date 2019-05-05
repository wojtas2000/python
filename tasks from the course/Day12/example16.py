class Kolo:
    def __init__(self, promien):
        self.__promien = promien

    @property
    def promien(self):
        return self.__promien

    @promien.setter
    def promien(self, value):
        if value < 0:
            raise ValueError
        self.__promien = value

    @property
    def obwod(self):
        return self.__promien * 2 * 3.14

    @obwod.setter
    def obwod(self, value):
        self.__promien = value / (3.14 * 2)


a = Kolo(100)
a.promien = 50
print(a.promien, a.obwod)
a.obwod = 100
print(a.obwod, a.promien)

# a.promien = -12  # rzuci blad!