# otworz plik csv zad9.csv zawierajacy imiona i nazwiska i wypisz na ekran w kazdej lini - najpierw nazwisko potem imię, oddzielone spacją
import csv

with open('zad9.csv') as plik:
    reader = csv.reader(plik)
    for row in reader:
        print(row[1], row[0])