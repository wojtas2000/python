class Kolo:
    def __init__(self, promien):
        self.__promien = promien

    @property
    def promien(self):
        return self.__promien

    @property
    def obwod(self):
        return self.__promien * 2 * 3.14


a = Kolo(100)
print(a.promien)
print(a.obwod)
