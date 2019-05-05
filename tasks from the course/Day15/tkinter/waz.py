import random


class Punkt:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def czy_sie_nakladaja(self, inny_punkt):
        return self.x == inny_punkt.x and self.y == inny_punkt.y

    @classmethod
    def losuj(cls, max_x, max_y):
        x = random.randint(0, max_x)
        y = random.randint(0, max_y)
        return cls(x, y)


class Waz(Punkt):
    def __krok(self, roznica):
        if roznica > 0:
            return -1
        if roznica < 0:
            return 1
        return 0

    def zrob_krok(self, cel):
        roznica_x = self.x - cel.x
        roznica_y = self.y - cel.y
        self.x += self.__krok(roznica_x)
        self.y += self.__krok(roznica_y)


if __name__ == '__main__':
    jedzonko = Punkt.losuj(500, 500)
    waz = Waz.losuj(500, 500)
    while not jedzonko.czy_sie_nakladaja(waz):
        waz.zrob_krok(jedzonko)
        print(waz.x, waz.y)
