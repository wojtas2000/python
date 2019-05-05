def dodawanie(a, b):
    return a + b


def funkcja(liczba):
    wynik = 0
    for a in range(0, liczba):
        wynik = dodawanie(wynik, a)
    return wynik


print(funkcja(10))
