"""
Zad 3.
program wypisuj¹cy tabliczkê mnozenia (1 do 10) dla podanej przez u¿ytkownika liczby
np gdy uzytkownik podal 3:
3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
itd..."""

podana_liczba = int(input("Podaj liczbê a wypiszê mno¿enie do 10 z t¹ liczb¹: "))

mnozenie = 0
mnoznik = 1

while mnozenie < 10:
    print("{} x {} = {}".format(podana_liczba, mnoznik, (podana_liczba * mnoznik)))
    mnozenie += 1
    mnoznik += 1