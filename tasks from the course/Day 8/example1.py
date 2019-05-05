d = 0


def funkcja(a, b, c):
    print("wszystkie zmienne", a, b, c)
    a = a + b
    print("linia 7", a)
    a = a + d
    print("linia 9", a)
    return a


wynik = funkcja(10, 5, 3)
print(wynik)
