# napisz program funkcje ktora przyjmuje liste i liczbe.
# powinna ona zwrocic element z listy pod tym indeksem lub None jezeli nie ma tego indeksu
# nie uzywaj ifow


def get_from_list(lista, index):
    try:
        return lista[index]
    except IndexError:
        return None


# nie przejmuj sie tym co ponizej, jak będzie dobra funkcja to wszystko zadziała ;)
assert get_from_list([1, 2, 3], 0) == 1
assert get_from_list([1, 2, 3], 4) == None
