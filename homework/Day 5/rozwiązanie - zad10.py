# Napisz program ktory znajdzie wszystkie powtorzenia w liscie

moja_lista = [0, 1, 1, 'a', 2, 'abc', 'x', ['lista2', ''], 'a', '', 'z', 99, 't', 'www']

odwiedzone = []
powtorzenia = []

for element in moja_lista:
    if element in odwiedzone:  # juz go kiedys spotkalismy
        powtorzenia.append(element)
    else:  # widzimy go pierwszy raz, dodajmy do odwiedzonych
        odwiedzone.append(element)

print(powtorzenia)
