"""TRUDNIEJSZE - DLA CHETNYCH (moze byc do domu)
uzywajac klasy Ksiazka z zad4 napisz klase Biblioteka
- ktora trzyma liste ksiazek (na poczatku pusta)
- posiada metode dodaj_ksiazke(self, ksiazka) dodajaca ksiazke do listy
- posiada metode usun_ksiazke(self, ksiazka) usuwajaca ksiazke
- posiada dostep za pomoca [] (jak lista lub slownik) gdzie przyjmowany jest numer isbn
a zwracana ksiazka o tym numerze lub blad jesli nie ma (magiczna metoda __getitem__ )
- posiada obsluge funkcji len() zwracajca ilosc ksiazek
- dla chętnych dodatkowe metody obslugi "ala slownik" (przypisywanie i usuwanie elementow)
pełen opis magicznych metod w Pythonie: https://rszalski.github.io/magicmethods/

przykladowe uzycie:

biblioteka = Biblioteka()
biblioteka.dodaj_ksiazke(Ksiazka('Terror', 'Dan Simmons', '12345')
biblioteka['12345'] - zwraca ksiazke Terror
len(biblioteka) - zwraca 1
biblioteka['22222'] - rzuca blad

"""

