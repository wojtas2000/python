# Napisz klasę Czlowiek przyjmujaca w konstruktorze "imie" i "nazwisko"
# Napisz dziedzicaca klase Student
# Napisz konstuktor klasy Student tak by przyjmował trzy argumenty - te same co Czlowiek + nr_indeksu
# Ustaw wszystkie atrybuty nie powtarzajac w klasie Student kodu (uzyj konstruktora klasy Czlowiek)

class Czlowiek:
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko


class Student(Czlowiek):
    def __init__(self, imie, nazwisko, nr_indeksu):
        super().__init__(imie, nazwisko)
        # Czlowiek.__init__(self, imie, nazwisko)
        self.nr_indeksu = nr_indeksu


stud = Student("Bartek", "Biernacki", 2133333)
print(stud.imie)
print(stud.nr_indeksu)


