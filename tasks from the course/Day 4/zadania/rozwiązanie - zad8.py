"""
Przyjmuje od uzytkownika napis i wyswietla “Access allowed” jesli uzytkownik wpisal
"haslo" lub “Access denied” w przeciwnym wypadku.

W przypadku wypisania “Acces denied” ponawia prosbe o wpisanie hasla.
Po pięciu nieudanych probach przestaje probowac dalej.
"""
udalo_sie = False

for proba in range(0, 5):
    haslo = input("Podaj haslo: ")
    if haslo == 'haslo':
        print("Access allowed.")
        udalo_sie = True
        break
    print("Access denied")

if udalo_sie:
    print("Udalo sie!")