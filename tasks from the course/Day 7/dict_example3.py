slownik = {
    'klucz': 'wartosc'
}

if "klucz" in slownik:
    print("Klucz jest w slowniku")

if "nieklucz" in slownik:
    print("Tego nie ma wiec do tego printa nie wejdziemy")


slownik.update({"klucz1": "wartosc"})
print(slownik)
slownik.update({"klucz1": "inna wartość", "klucz2": "wartosc"})
print(slownik)
print(slownik["klucz2"])
