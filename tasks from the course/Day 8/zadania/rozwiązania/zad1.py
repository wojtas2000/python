# Napisz program przyjmujacy floata i wypisujacy go na ekran. W przypadku gdy uzytkownik poda cos inngego niz float wypisz
# "Musisz podac liczbe!"
# nie uzywaj ifów

napis = input("Podaj liczbę: ")
try:
    liczba = float(napis)
    print(liczba)
except ValueError:
    print("Musisz podac liczbe!")