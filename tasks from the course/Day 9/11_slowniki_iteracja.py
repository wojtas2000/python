slownik = {
    "klucz1": "wartosc",
    "klucz2": "wartosc",
}

for klucz in slownik:
    wartosc = slownik[klucz]
    print(klucz, wartosc)

for wartosc in slownik.values():
    print(wartosc)

for klucz, wartosc in slownik.items():
    print(klucz, wartosc)
