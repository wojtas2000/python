slownik = {
    "klucz": "wartosc",
    "klucz2": "wartosc",
    "klucz3": "wartosc",
}
print(slownik)

for klucz in slownik:  # iterujemy po kluczach
    print(klucz)
    print(slownik[klucz])

for klucz, wartosc in slownik.items():  # iterujemy po kluczach i wartosciach
    print(klucz)
    print(wartosc)

for wartosc in slownik.values():  # iterujemy po samych wartosciach
    print(wartosc)
