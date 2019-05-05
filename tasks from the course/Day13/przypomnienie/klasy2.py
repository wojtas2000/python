class Zwierze(object):
    def __init__(self):
        print("Wywolam sie podczas tworzenia instancji klasy!")

    def zyj(self):
        print("Zyje!")


class Kon(Zwierze):
    def __init__(self, imie):
        Zwierze.__init__(self)
        self.imie = imie

    def daj_glos(self):
        print("ihaaa")


class Osiol(Zwierze):
    def __init__(self, imie):
        super().__init__()
        self.imie = imie

    def daj_glos(self):
        print("iooooiooo")


class Mul(Kon, Osiol):
    pass


mul = Mul("Kon")
mul.daj_glos()
mul.zyj()


