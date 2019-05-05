slownik = {
    "klucz": "wartosc",
    "klucz2": "wartosc"
    # mapa kluczy na wartosci, bez ustalonej kolejnosci
    # klucze muszą być unikalne, musza byc wartosciami niezmiennymi
}

print(slownik["klucz"])
slownik["nowy_klucz"] = "nowa wartość"
# slownik["nie ma"]  - rzuci blad KeyError, jesli klucza nie ma
zmienna = slownik.get("nie ma")  # zwroci nam None jesli klucza nie ma
zmienna = slownik.get("nie ma", 123)  # zwroci 123 jesli klucza nie ma
