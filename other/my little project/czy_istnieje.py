import csv


def jest(imie, nazwisko):
    """sprawdza czy dane wpisy istnieją w bazie, jesli tak True, jeśli nie False"""

    with open("baza.csv", "r") as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for line in csv_reader:
            if line["Imie"] == imie and line["Nazwisko"] == nazwisko:
                return True
