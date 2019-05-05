def nazwa_funkcja(argument):
    print(argument)


nazwa_funkcja("jakiś napis")


def funkcja_z_zerem_argumentow():
    pass

funkcja_z_zerem_argumentow()


def funkcja_z_domyslna(argument_wymagany, argument_domyslny="jakas wartosc", arg2=""):
    # najpierw deklarujemy wszystkie argumenty wymagane
    # a potem opcjonalne (domyslne)
    pass


funkcja_z_domyslna("tylko wymagany")
funkcja_z_domyslna("wymagany", "opcjonalny", "opcjonalny2")
funkcja_z_domyslna("wymagany", argument_domyslny="opcjonalny")
funkcja_z_domyslna("wymagany", arg2="arg2")


def funkcja2(arg_opcjonalny=[]):
    # arg domyslny jest przypisywany w momencie tworzenia funkcji
    # taka lista będzie wspolna dla wszystkich wywolan!
    return arg_opcjonalny


def funkcja3(arg_opcjonalny=None):
    # ten kod zadziala zgodnie z oczekiwaniami
    if arg_opcjonalny is None:
        arg_opcjonalny = []
    return arg_opcjonalny
