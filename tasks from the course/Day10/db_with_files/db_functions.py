NAZWA_PLIK = "db.txt"


def wczytaj_baze():
    baza = []
    with open(NAZWA_PLIK) as plik:
        for wpis in plik.readlines():
            baza.append(wpis.strip())
    return baza


def zapisz_baze(baza):
    with open(NAZWA_PLIK, 'w') as plik:
        for wpis in baza:
            plik.write('{}\n'.format(wpis))


def name_exists(name):
    names_list = wczytaj_baze()
    name = str(name).upper()
    return name in names_list


def add_to_list(name):
    names_list = wczytaj_baze()
    if name_exists(name):
        print("Imię {} jest już w kontaktach".format(name))
    else:
        names_list.append(name)
        print("Imię {} zostało dodane do kontaktów".format(name))
        zapisz_baze(names_list)


def count_name():
    names_list = wczytaj_baze()
    return len(names_list)


def print_names():
    names_list = wczytaj_baze()
    print(names_list)


def remove_from_list(name):
    names_list = wczytaj_baze()
    if name_exists(name):
        names_list.remove(name)
        print("Imię {} zostało usunięte".format(name))
        zapisz_baze(names_list)
    else:
        print("Brak imienia na liście")
