# napisz funkcję, która przyjmuję liczbę i rzuca wyjątek ValueError jeśli liczba nie jest w zakresie 0-10
# jeśli jest funkcja powinna zwrócic 0


def super_funkcja(liczba):
    if 0 <= liczba <= 10:
        return 0
    else:
        raise ValueError("Liczba poza zakresem")


# nie przejmuj sie tym co ponizej, jak będzie dobra funkcja to wszystko zadziała ;)
assert super_funkcja(3) == 0
try:
    super_funkcja(-1)
    raise AssertionError("Funkcja nie rzucila wyjątku dla -1!!")
except ValueError:
    pass
try:
    super_funkcja(11)
    raise AssertionError("Funkcja nie rzucila wyjątku dla 11!!")
except ValueError:
    pass
