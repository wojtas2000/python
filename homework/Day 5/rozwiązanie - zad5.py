"""
Wypisuj po kolei elementy z listy za pomoca petli for az napotkasz podzielny przez 5 - wtedy przerwij petle.
"""

moja_lista = [1, 2, 3, 7, 4, 2, 15, 8, 12, 7, 0]

for liczba in moja_lista:
    print(liczba)
    if liczba % 5 == 0:
        break
