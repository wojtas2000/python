import sprawdz
import csv
import czy_istnieje


def dodaj_wpis():
    """funkcja dodająca wpis do bazy danych, inforumuje
    jeśli istnieje już w bazie"""

    imie = (input("Dodaj imię:").strip()).capitalize()
    nazwisko = (input("Dodaj nazwisko:").strip()).capitalize()

    if sprawdz.czy_poprawnie(imie, nazwisko):
        if czy_istnieje.jest(imie, nazwisko):
            print("Jest w bazie, pomijam.\n")
        else:
            with open("baza.csv", "a", newline='') as file:
                filed_name = ['Imie', 'Nazwisko']
                file_append = csv.DictWriter(file, fieldnames=filed_name)
                file_append.writerow({"Imie":imie, "Nazwisko":nazwisko})
            print("Wpis \"{} {}\" został dodany do bazy danych.\n".format(imie, nazwisko))
