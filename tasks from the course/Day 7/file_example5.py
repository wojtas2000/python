with open("example.txt") as plik:
    for linia in plik:
        print(linia, end="")
print()
print("drugi raz")
with open("example.txt") as plik:
    for linia in plik:
        print(linia.strip())  # metoda strip wyrzuca biale znaki z poczatku i konca stringa
    plik.seek(0)  # znowu mozemy odczytywac plik od poczatku
