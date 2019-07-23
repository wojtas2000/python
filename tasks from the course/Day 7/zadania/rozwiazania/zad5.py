# dopisz do pliku zad5.txt nowa linie "Ala go kocha, a kot ją wcale"

with open('zad5.txt', 'a', encoding='utf-8') as plik:  # tryb "dopisywania do pliku"
    plik.write("\n")  # pamiętajmy o znakach nowej lini
    plik.write("Ala go kocha, a kot ją wcale")
