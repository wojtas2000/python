try:
    raise ValueError
except ValueError:
    print("Zlapano ValueError")


def dodawanie(a, b):
    try:
        a = int(a)
        b = int(b)
    except ValueError:
        raise ValueError("Musisz podac tu liczby")
    return a + b


try:
    dodawanie("a", 1)
except ValueError as zmienna_z_wyjatkiem:
    print("no jaaaa")
    print(zmienna_z_wyjatkiem)
