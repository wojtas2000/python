zmienna_globalna = "wartosc"
zmienna_a = "tez globalna ;)"


def funkcja1():
    zmienna_lokalna = "lokalna wartosc"
    print(zmienna_lokalna)
    # spoza funkcji nie mozemy dostac sie do zmiennej lokalnej
    print(zmienna_globalna)

# do zmiennej globalnej mozemy dostac się w kazdym momencie
print(zmienna_globalna)


def funkcja2():
    zmienna_a = "lokalna"
    # to jest zmienna lokalna, nie ma wplywu na zmienna globalna
    global zmienna_globalna # w ten sposob mozemy zmienic zmienna globalna
    zmienna_globalna = "zmieniona globalna"


def funkcja3():
    zmienna_lokalna_funkcji3 = "xxx"

    def funkcja_wew():
        # funkcja_wew ma dostęp do zmiennych lokalnych funkcja3
        zmienna_lokalna = "asd"
        print(zmienna_lokalna_funkcji3)

    # funkcja3 nie ma dostępu do zmiennych lokalnych funkcja_wew
