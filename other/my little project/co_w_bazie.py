import csv


def wyswietl_imiona():
    """funkcja wyświetlająca wszystkie wpisy w bazie"""

    print("Kontakty w bazie:")

    with open("baza.csv", "r") as file:
        csv_reader = csv.reader(file)

        lista = []

        next(csv_reader)

        for line in file:
            line = line[:-1].split(",")
            lista.append(line)
            print("{}.".format((lista.index(line))+1), line[0], line[1])
    print()
