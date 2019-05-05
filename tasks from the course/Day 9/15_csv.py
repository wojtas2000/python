import csv

with open('arkusz.csv') as uchwyt:
    arkusz = csv.reader(uchwyt)
    for wiersz in arkusz:
        print(wiersz)

with open('arkusz.csv') as uchwyt:
    arkusz = csv.DictReader(uchwyt)
    for wiersz in arkusz:
        print(dict(wiersz))
        print(wiersz["Nazwa"])
