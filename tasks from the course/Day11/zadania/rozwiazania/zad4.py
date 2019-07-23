# Napisz klase Ksiazka zawierajaca atrybuty:
# Tytul, Autor, numer ISBN, ilosc stron
#
# Dopisz magiczne metody obslugujace:
# print(ksiazka) - zwraca stringa "{autor} - {tytul}" - __str__(self)
# len(ksiazka) - zwraca ilosc stron ksiazki - __len__(self)
# ksiazka1 == ksiazka2 - sprawdza czy sa to te same ksiazki porownujac numery ISBN -  __eq__(self, other)


class Ksiazka:
    def __init__(self, tytul, autor, isbn, ilosc_stron):
        self.ilosc_stron = ilosc_stron
        self.isbn = isbn
        self.autor = autor
        self.tytul = tytul

    def __str__(self):
        return "{autor} - {tytul}".format(
            autor=self.autor,
            tytul=self.tytul
        )

    def __len__(self):
        return self.ilosc_stron

    def __eq__(self, other):
        if not isinstance(other, Ksiazka):
            return False
        return other.isbn == self.isbn


pan_tadeusz = Ksiazka("Pan Tadeusz", "Adam Mickiewicz", 123456, 200)
print(pan_tadeusz)
print(len(pan_tadeusz))

terror = Ksiazka("Terror", "Dan Simmons", 555545, 300)

print(terror == pan_tadeusz)

wcale_nie_pan_tadeusz = Ksiazka("Podszywam sie pod Pana Tadeusza",
                                "Bartlomiej Biernacki", 123456, 100)
print(wcale_nie_pan_tadeusz == pan_tadeusz)
