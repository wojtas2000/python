"""
Napisz program ktory wypisuje podane slowo od tylu (z uzyciem petli!)
"""

napis = input()
# wersja 1
for indeks in range(len(napis) - 1, -1, -1):
    print(napis[indeks], end='')
print()

# wersja 2
wynik = ''
for litera in napis:
    wynik = litera + wynik
print(wynik)

