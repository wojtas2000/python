plik = open("example.txt", mode="r", encoding="utf-8")  # jak nie podamy trybu to otwarty jest w trybie "read"
print("plik otwarty")
plik.close()
print("plik zamkniety")

with open("example.txt") as plik:  # polecana metoda pracy z plikami!
    print("plik otwarty")
print("plik zamkniety")
