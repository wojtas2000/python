# napisz program wypisujacy utworzona ponizej liste i znajdujacy najmniejsza i najwieksza wartosc w niej.
# Program powinien wypisac:
# Zawartosc listy: [<<dane>>]
# Maxymalna wartosc: <<wartosc>> <<pozycja w liscie>>
# Minimalna wartosc: <<wartosc>> <<pozycja w liscie>>
import random
moja_lista = list(random.sample(range(50), 10))

print(moja_lista)

max_wartosc = float('-inf')
max_index = -1
min_wartosc = float('inf')
min_index = -1

for indeks, wartosc in enumerate(moja_lista):
    if wartosc > max_wartosc:
        max_wartosc = wartosc
        max_index = indeks
    if wartosc < min_wartosc:
        min_wartosc = wartosc
        min_index = indeks

print("")
print("Maxymalna wartosc: {} {}".format(max_wartosc, max_index))
print("Minimalna wartosc: {} {}".format(min_wartosc, min_index))
