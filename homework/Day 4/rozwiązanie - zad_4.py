"""
Zad 4*.
Napisz program realizujacy szyfr ROT13 (https://pl.wikipedia.org/wiki/ROT13) -
kazda litere w wejsciowym stringu zamien na litere odlegla w alfabecie o 13 znakow
(zalozmy 26 lliter w alfabeciem bez polskich znakow, tylko male liter).

Czyli np. a -> n, b -> o, z -> m

Poprawnoœæ mozna miedzy innymi sprawdzic w ten sposob,
ze dwukrotne zaszyfrowanie daje odszyfrowany tekst.

a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z,
"""

alfabet = "abcdefghijklmnopqrstuvwxyz " # ostatni znak to spacja

napis_wej = input("Wpisz has³o do zaszyfrowania: ")

print(napis_wej)
litera = ''

# for i in napis_wej:
#
#     litera = alfabet.find(i)
#     if litera > 12:
#         print(litera, " - ", i, "zmieniona to:", alfabet[litera - 13])
#     elif litera < 12:
#         print(litera, " - ", i, "zmieniona to:", alfabet[litera + 13])

for i in napis_wej:
    litera = alfabet.find(i)
    if litera >= 13:
        print(alfabet[litera - 14], end='')
    elif litera < 13:
        print(alfabet[litera + 14], end='')


