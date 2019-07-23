# wczytaj plik zad9.csv nastepnie utworz nowy plik csv zad10.csv zawierajacy wpierw nazwisko, potem imie
# a w trzeciej kolumnie losowa liczbe z zakresu 0-100 oznaczajaca ilosc pkt z egzaminu

import csv
import random

dane = []

with open('zad9.csv') as wejscie:
    reader = csv.reader(wejscie)
    for row in reader:
        dane.append([row[1], row[0], random.randint(0, 100)])

with open('zad10.csv', 'w') as wyjscie:
    writer = csv.writer(wyjscie)
    writer.writerows(dane)