import dodaj_wpis
import co_w_bazie
import czy_imie
import usun
import liczba_imion

koniec = 1

menu = "MENU PROGRAMU \"KONTAKTY\"\n\
1. Dodanie kontaktu  \n\
2. Wyświetlenie kontaktów z bazy \n\
3. Sprawdzenie czy podany kontakt jest w bazie \n\
4. Usunięcie wpisu z bazy \n\
5. Sprawdzenie ilości kontaktów w bazie \n\
9. Zakończenie programu.\n"

while koniec != 0:

    print(menu)
    wybor = 0

    try:
        wybor = int(input("Aby wybrać z menu wpisz cyfrę: "))
    except ValueError:
        pass

    if 0 < wybor < 6 or wybor == 9:
        if wybor == 1:
            dodaj_wpis.dodaj_wpis()
        if wybor == 2:
            co_w_bazie.wyswietl_imiona()
        if wybor == 3:
            czy_imie.czy_imie()
        if wybor == 4:
            usun.usun_imie()
        if wybor == 5:
            liczba_imion.ile_imon()
        if wybor == 9:
            koniec = 0
    else:
        print("Podałeś błędne dane, sprubój ponownie.\n")