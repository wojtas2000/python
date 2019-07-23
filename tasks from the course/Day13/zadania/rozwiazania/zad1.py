# Napisz program przyjmujacy liczby z lini komend i wypisujacy na ekran sumę tych liczb
# Gdy użytkownik nie podal zadnego argumentu wypisuje poniższą informację "how to use":
# Program sumujący liczby. Użycie `python zad.1.py [liczby]`
# np. `python zad1.py 1 2 3` wypisze na ekran 6

import sys

if len(sys.argv) < 2:
    print("Program sumujący liczby. Użycie `python {} [liczby]`".format(sys.argv[0]))
    print("np. `python zad1.py 1 2 3` wypisze na ekran 6")
    exit(1)

wynik = 0
for i in sys.argv[1:]:
    wynik += int(i)

print(wynik)
