# Zad 1.
# Przyjmuje od uzytkownika napis i wyswietla “Access allowed” jesli uzytkownik wpisal
# "haslo" lub “Access denied. This incident will be reported.” w przeciwnym wypadku.
#
# https://imgs.xkcd.com/comics/incident.png

haslo = input("Podaj haslo: ")
if haslo == 'haslo':
    print("Access allowed")
else:
    print("Access denied. This incident will be reported.")
