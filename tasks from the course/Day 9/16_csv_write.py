import csv

with open('arkusz2.csv', 'w') as uchwyt:
    writer = csv.writer(uchwyt)
    rows = [
        ['Nazwa', 'Cena'],
        ['Linia stalowa', 12],
        ['Kamizelka asekuracyjna', 50]
    ]
    writer.writerows(rows)
