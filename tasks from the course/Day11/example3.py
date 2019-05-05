class Zwierze:
    def __init__(self, imie):
        self.imie = imie

    def zyj(self):
        print("Zyje!")

    def daj_glos(self):
        pass


class Czlowiek(Zwierze):
    def daj_glos(self):
        print("Hello!")


class Kot(Zwierze):
    def daj_glos(self):
        print("Miau miau")


class Student(Czlowiek):
    def __init__(self, imie, nr_albumu):
        super().__init__(imie)
        self.nr_albumu = nr_albumu


zwierze = Zwierze("abstrakcyjne zwierze")
print(zwierze.imie)
zwierze.daj_glos()
zwierze.zyj()

print("======================")
puszek = Kot("Puszek")
print(puszek.imie)
puszek.daj_glos()
puszek.zyj()

print("======================")
student_bartek = Student("Bartek", 123456)
print(student_bartek.imie)
print(student_bartek.nr_albumu)

print("======================")
print(isinstance(student_bartek, Student))
print(isinstance(student_bartek, Kot))
print(isinstance(student_bartek, Zwierze))

print("----------------------")
czlowiek_stefan = Czlowiek("Stefan")
print(isinstance(czlowiek_stefan, Student))
print(isinstance(czlowiek_stefan, Kot))
print(isinstance(czlowiek_stefan, Czlowiek))
print(isinstance(czlowiek_stefan, Zwierze))
