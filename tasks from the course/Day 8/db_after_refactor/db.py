import db_functions

welcome_message = "Baza danych\
\nWybierz opcję:\
\nWyszukaj imie, naciśnij klawisz 1:\
\nDodaj imie, naciśnij klawisz 2:\
\nUsuń imie, naciśnij klawisz 3:\
\nWyświetl liczbę imion, naciśnij klawisz 4:\
\nWyświetl listę imion, naciśnij klawisz 5:\
\nZakończ program, naciśnij klawisz 0:\n"


response = input(welcome_message)
while response != "0":
    if response == "1":
        name = input("Podaj wyszukiwane imię: ")
        if db_functions.name_exists(name):
            print("Imię {} jest już w kontaktach".format(name))
        else:
            print("Imię {} nie zostało odnalezione".format(name))
    elif response == "2":
        name = input("Dodaj imię do listy: ")
        db_functions.add_to_list(name)
    elif response == "3":
        name = input("Podaj imię, które chcesz usunąć: ")
        db_functions.remove_from_list(name)
    elif response == "4":
        print("Liczba imion na liście to {}".format(db_functions.count_name()))
    elif response == "5":
        db_functions.print_names()
    else:
        print("Podałeś złę polecenie, spróbuj ponownie.")

    response = input("Podaj nowe polecenie\n")
