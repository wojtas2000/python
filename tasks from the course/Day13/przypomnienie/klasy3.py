class Klasa1:
    atrybut_klasowy = 12

    @staticmethod
    def metoda_statyczna():
        print("metoda statyczna")

    @classmethod
    def metoda_klasowa(cls):
        print("metoda klasowa z klasy ", cls)

    @classmethod
    def zwroc_instancje(cls):
        return cls()


class Klasa2(Klasa1):
    pass


Klasa1.metoda_statyczna()
Klasa1.metoda_klasowa()
Klasa2.metoda_klasowa()

instancja1 = Klasa1()
instancja2 = Klasa1.zwroc_instancje()
print(instancja1, instancja2)
