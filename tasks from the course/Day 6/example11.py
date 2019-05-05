zmienna = "globalna"


def funkcja():
    global zmienna
    zmienna = "zmieniona wewnatrz funkcji"


print(zmienna)
funkcja()
print(zmienna)
