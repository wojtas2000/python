# napisz klase Student przyjmujaca w konstruktorze imie i posiadajacy metode "przedstaw_sie"
# wypisujaca na ekran "mam na imie {imie}"
# stworz instancje tej klasy z wlasnym imieniem i wywolaj "przedstaw_sie"

class Student:
    def __init__(self, imie_studenta):
        self.imie = imie_studenta

    def przestaw_sie(self):
        print("Mam na imię {}".format(self.imie))


student_bartek = Student("Bartek")
student_bartek.przestaw_sie()
