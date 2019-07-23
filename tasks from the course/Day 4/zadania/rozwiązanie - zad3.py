"""
Dla kazdej liczby pomiedzy 0 a 16384 wypisz czy jest parzysta czy nie.
"""

for liczba in range(0, 16385):
    if liczba == 0:
        print("Ani nie parzysta ani parzysta!")
    elif liczba % 2 == 0:
        print("Parzysta")
    else:
        print("Nieparzysta")
