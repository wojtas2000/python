zmienna = "globalna"


def funkcja1():
    print(zmienna)


funkcja1()
zmienna = "zmieniona globalna"
funkcja1()  # funkcja wypisze wartosc zmiennej w momencie wywolania
