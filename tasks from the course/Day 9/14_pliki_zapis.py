with open("14_zapis.txt", 'w', encoding="utf-8") as uchwyt:
    # usuwamy zawartosc pliku jesli istnieje i zapisujemy nowa
    uchwyt.write("hello world!")

with open("14_zapis.txt", 'w', encoding="utf-8") as uchwyt:
    uchwyt.writelines(["linia1\n", "linia2\n"])
    # writelines NIE dodaje znaków konca linii

with open("14_zapis.txt", 'r+', encoding="utf-8") as uchwyt:
    uchwyt.write("nadpisujemy\n")
    print(uchwyt.readline())

with open("14_zapis.txt", "a", encoding="utf-8") as uchwyt:
    # nie usunie zawartosci pliku, dopisze na koncu
    uchwyt.write("append")
