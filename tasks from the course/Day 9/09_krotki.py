krotka = (1, 2, 3)

# del krotka[0]   # nie mozemy usunac
# krotka.append('a')   # nie mozemy dodac


def funkcja(arg_domyslny=(1, 2, 3)):
    return 1, 2  # zwracamy wiecje niz jedna wartosc poprzez zwrocenie krotki


zmienna1, zmienna2, zmienna3 = krotka

wynik1, wynik2 = funkcja()

a = 12
b = 8

# zamiana zmiennych miejscami
tmp = a
a = b
b = tmp
# ten zapis robi to samo, tylko krocej i bez zmiennej pomocniczej :)
b, a = a, b
