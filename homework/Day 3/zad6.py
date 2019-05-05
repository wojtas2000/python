"""
Zad 6.
Oblicz czy podany rok jest przestępny
Czyli podzielny przez 4 oraz niepodzielny przez 100 lub podzielny przez 400
"""

rok = int(input("Podaj rok: "))

if (rok % 4 == 0 and rok % 100 != 0) or rok % 400 == 0:
    print("Przestepny")
else:
    print("Nie przestepny")
