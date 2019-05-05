zmienna = "globalna"


def funkcja1():
    zmienna = "lokalna"
    print(zmienna)


funkcja1()
zmienna = "zmieniona globalna"
funkcja1()  # na funkcje nie ma wplywu wartosc zmiennej globalnej
