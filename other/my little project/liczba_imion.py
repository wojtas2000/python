import csv


def ile_imon():
    """funkcja wyświetlająca ile imion jest w bazie"""

    with open("baza.csv", "r") as csv_file:
        csv_reader = csv.DictReader(csv_file)

        ile = []

        for line in csv_reader:

            ile.append(line["Imie"])
        print("Ilość wpisów w bazie: {} \n".format(len(ile)))
