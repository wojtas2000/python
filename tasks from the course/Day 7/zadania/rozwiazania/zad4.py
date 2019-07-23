# wczytaj plik zad4.txt zawierajacy liczby w kolejnych wierszach i wypisz na ekran sumę tych liczb

with open('zad4.txt') as plik:
    suma = 0
    for linia in plik:
        suma += int(linia)

print(suma)
