names_list = []


def name_exists(name):
    name = str(name).upper()
    return name in names_list


def add_to_list(name):
    if name_exists(name):
        print("Imię {} jest już w kontaktach".format(name))
    else:
        names_list.append(name)
        print("Imię {} zostało dodane do kontaktów".format(name))


def count_name():
    return len(names_list)


def print_names():
    print(names_list)


def remove_from_list(name):
    if name_exists(name):
        names_list.remove(name)
        print("Imię {} zostało usunięte".format(name))
    else:
        print("Brak imienia na liście")
