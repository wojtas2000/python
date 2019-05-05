"""
Zad 3.
Sprawdź czy liczba jest podzielna przez 3, 5, 7. Wypisac odpowiednie komunikaty.

Do sprawdzenia podzielnosci mozna uzyc znaku a%b - reszta z dzielenia a przez b. Liczba podzielna ma resztę z dzielenia równą 0.
"""

liczba = int(input("Podaj liczbe:"))

if liczba % 3 == 0:
    print("Podzielna przed 3")

if liczba % 5 == 0:
    print("Podzielna przed 5")

if liczba % 7 == 0:
    print("Podzielna przed 7")
