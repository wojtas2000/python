# otworz plik 'zad11.csv' zawierajacy arkusz z zakupionymi towarami
# 1) policz naleznosc za caly rachunek (sume ilosci sztuk x cena jednostkowa) i wypisz na ekran
# 2) stworz plik 'zad11-output.csv' zawierajacy dane z pliku zad11.csv wraz z dodatkowa kolumna "wartość" zawierajaca naleznosci za poszczegolny wiersz (cena jednostkowa x ilosc)
# oraz dodatkowa pozycja (wierszem) SUMA zawierajaca puste komorki w pod "ilosc" i "cena jednostkowa" i sume calego zamowienia pod "wartość"
import csv

suma = 0
wyjscie = []

with open('zad11.csv', encoding='utf-8') as csv_file:
    reader = csv.DictReader(csv_file)
    # DictReader - specjalny rodzaj csv readera ktory potrafi czytac naglowek
    # i jako wiersze zwraca slowniki z kluczami bedacymi naglowkami kolumn
    for row in reader:
        wartosc = float(row['Cena jednostkowa (PLN)']) * int(row['Ilość'])
        suma += wartosc
        row['Wartość'] = wartosc
        wyjscie.append(row)

wyjscie.append({
    'Produkt': 'Suma',
    'Ilość': '',
    'Cena jednostkowa (PLN)': '',
    'Wartość': suma
})

field_names = ['Produkt', 'Ilość', 'Cena jednostkowa (PLN)', 'Wartość']
with open('zad11-output.csv', 'w', newline='', encoding='utf-8') as plik:
    writer = csv.DictWriter(plik, fieldnames=field_names)
    writer.writeheader()
    writer.writerows(wyjscie)