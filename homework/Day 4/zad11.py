"""
Napisz program mnozacy dwie liczby uzywajac tylko operacji dodawania.
"""

a = int(input("podaj a: "))
b = int(input("podaj b: "))
wynik = 0
for i in range(b):
    wynik = wynik + a

print(wynik)