# ponizsza lista zawiera krotki (tuple) z zakupionymi produktami oraz ich zakupiona lioscia.
# Stworz slownik, gdzie kluczami sa produkty a wartosciami zakupione ilosci.
# UWAGA: niektóre produkty na liscie sie powtarzaja (kasier czasami zamiast wpisac ilosc produktu skasowal go kilkukrotnie...)
# w takim wypadku nalezy zsumowac ilosc danego produktu

produkty = [('jajko', 4), ('mąka', 1), ('proszek do pieczenia', 1), ('proszek do pieczenia', 1), ('mleko', 2),
            ('jajko', 4), ('maslo', 1), ('cukier puder', 1), ('mąka', 2), ('orzechy', 1), ('marchewka', 2)]


wynik = {}
for prod in produkty:
    nazwa = prod[0]
    ilosc = prod[1]
    if nazwa not in wynik:
        wynik[nazwa] = ilosc  # tworzymy nowy klucz z tym wpisem
    else:
        wynik[nazwa] += ilosc  # dodajemy do istniejacej wartosci

print(wynik)
