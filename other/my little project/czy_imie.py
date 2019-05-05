import sprawdz
import czy_istnieje


def czy_imie():
    """funkcja sprawdzająca czy podany kontakt znajduje się w bazie"""

    imie = (input("Dodaj imię:").strip()).capitalize()
    nazwisko = (input("Dodaj nazwisko:").strip()).capitalize()

    if sprawdz.czy_poprawnie(imie, nazwisko):
        if czy_istnieje.jest(imie, nazwisko):
            print("Kontakt \"{} {}\" jest w bazie.\n".format(imie, nazwisko))
        else:
            print("Podanego kontaktu nie ma w bazie.\n")
