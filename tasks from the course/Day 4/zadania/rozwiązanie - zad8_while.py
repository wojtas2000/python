"""
Przyjmuje od uzytkownika napis i wyswietla “Access allowed” jesli uzytkownik wpisal
"haslo" lub “Access denied” w przeciwnym wypadku.

W przypadku wypisania “Acces denied” ponawia prosbe o wpisanie hasla.
Po pięciu nieudanych probach przestaje probowac dalej.

Wersja z uzyciem petli while
"""

wejscie = ''
proby = 0
while wejscie != 'haslo' and proby < 5:
    wejscie = input("Podaj haslo: ")
    if wejscie == "haslo":
        print("Access allowed")
    else:
        print("Access denied")
    proby += 1
    