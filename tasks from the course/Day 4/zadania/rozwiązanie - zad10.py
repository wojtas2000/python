"""
Napisz program który:
prosi o napis od uzytkownika
wypisuje ja malymi literami
jesli linia byla pusta konczy dzialanie, w przeciwnym wypadku wraca do pkt a)
"""
napis = 'dummy value'
print("Wpisuj linie aby zmienic na male litery, lub wpisz pusta aby zakonczyc")
while napis != '':
    napis = input()
    print(napis.lower())

