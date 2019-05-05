def dodaj_imie_zle(imie, lista_imion=[]):
    lista_imion.append(imie)
    return lista_imion


def dodaj_imie_dobre(imie, lista_imion=None):
    if lista_imion is None:
        lista_imion = []
    lista_imion.append(imie)
    return lista_imion


lista1 = dodaj_imie_zle("Ala")
lista2 = dodaj_imie_zle("Ola")
lista3 = dodaj_imie_zle("Aga")
