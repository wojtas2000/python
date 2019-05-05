def funkcja():
    zmienna = "lokalna"
    print(zmienna)


funkcja()
print(zmienna)  # blad! to zmiennej lokalnej nie ma dostępu spoza funkcji
