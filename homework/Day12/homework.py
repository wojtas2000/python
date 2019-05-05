# Homework
# 1) Zad 5 z Day 11
# 2)
# Przerób db_with_files z klasami (Day 11) tak, by:
# - nazwa_pliku byla atrybutem (pseudo)prywatnym
# - dodać metode statyczna "get_default_file_name()" zwracaja domyslna nazwe pliku (baza.txt)
# - metody nie uzywane przez database2.py powinny rowniez byc prywatne (get_db, write_db)
# - posiadaja atrybut (property) ilosc_wpisów, tylko do odczytu, zwracajacy zawsze aktualna ilosc w pliku
# (to samo co get_names_count())
# - rowniez "ilosc_wpisow" powinna byc zwracana z uzyciem funkcji len(instancja)
# - dodac metode klasowa "create_default_db()" tworzaca instancje klasy z domyslna nazwa plku
# (wzieta przed funkcje get_default_file_name())
