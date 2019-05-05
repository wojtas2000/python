class Klasa:
    def __init__(self):
        self.__priv = 12

    @property
    def priv(self):
        return self.__priv


a = Klasa()
print(a.priv)  # odwolujemy sie do takiej metody bez nawiasow
# a.priv = 12  # rzuci blad
