# stworz klase kwadrat przyjmujaca w konstruktorze bok kwadratu i posiadajaca dwie metody:
# pole - zwraca pole kwadratu
# obwod - zwraca obwod kwadratu

class Kwadrat:
    def __init__(self, bok):
        self.bok = bok

    def pole(self):
        return self.bok ** 2

    def obwod(self):
        return self.bok * 4


kwadrat_2 = Kwadrat(2)
print(kwadrat_2.pole())
print(kwadrat_2.obwod())

kwadrat_3 = Kwadrat(3)
print(kwadrat_3.obwod())
print(kwadrat_3.pole())
