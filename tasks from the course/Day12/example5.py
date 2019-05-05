class Db:
    DOMYSLNA_NAZWA = 'db.txt'

    def __init__(self, nazwa_plik=None):
        if nazwa_plik:
            self.nazwa_pliku = nazwa_plik
        else:
            self.nazwa_pliku = self.DOMYSLNA_NAZWA