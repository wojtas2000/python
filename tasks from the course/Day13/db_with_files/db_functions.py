class Database:
    def __init__(self, nazwa_pliku):
        self.__nazwa_pliku = nazwa_pliku

    @staticmethod
    def get_default_file_name():
        return 'baza.txt'

    @classmethod
    def create_default_db(cls):
        return cls(cls.get_default_file_name())

    @property
    def ilosc_wpisow(self):
        return self.count_name()

    def __len__(self):
        return self.count_name()

    def __wczytaj_baze(self):
        baza = []
        try:
            with open(self.__nazwa_pliku) as plik:
                for wpis in plik.readlines():
                    baza.append(wpis.strip())
            return baza
        except FileNotFoundError:
            return []

    def __zapisz_baze(self, baza):
        with open(self.__nazwa_pliku, 'w') as plik:
            for wpis in baza:
                plik.write('{}\n'.format(wpis))

    def name_exists(self, name):
        names_list = self.__wczytaj_baze()
        name = str(name).upper()
        return name in names_list

    def add_to_list(self, name):
        names_list = self.__wczytaj_baze()
        if self.name_exists(name):
            print("Imię {} jest już w kontaktach".format(name))
        else:
            names_list.append(name)
            print("Imię {} zostało dodane do kontaktów".format(name))
            self.__zapisz_baze(names_list)

    def count_name(self):
        names_list = self.__wczytaj_baze()
        return len(names_list)

    def print_names(self):
        names_list = self.__wczytaj_baze()
        print(names_list)

    def remove_from_list(self, name):
        names_list = self.__wczytaj_baze()
        if self.name_exists(name):
            names_list.remove(name)
            print("Imię {} zostało usunięte".format(name))
            self.__zapisz_baze(names_list)
        else:
            print("Brak imienia na liście")
