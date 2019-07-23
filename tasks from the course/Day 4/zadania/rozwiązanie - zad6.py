"""
Wypisz na ekran liczby od podanej przez uzytkownika do 0.
Uzytkownik moze podac tylko dodatnia, w przypadku podania liczby ujemnej wypisz blad.
"""

liczba = int(input("Podaj liczbe: "))

if liczba < 0:
    print("Zla liczba!")
    exit(1)  # konczy dzialanie programu - kod inny niz 0 oznacza ze
    # program zakonczyl sie bledem

for a in range(liczba, -1, -1):
    # ujemny krok sprawia, ze petla idzie od tylu
    # ale dalej koniec range'a jest "o jeden blizej" niz podany koniec
    print(a)
