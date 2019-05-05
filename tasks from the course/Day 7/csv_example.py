import csv

with open("plik.csv") as plik:
    reader = csv.reader(plik)
    for row in reader:
        print(row[0])
        print(row)


with open("plik.csv") as plik:
    reader = csv.DictReader(plik)
    for row in reader:
        print(row["Imie"])
        print(row["Nazwisko"])
