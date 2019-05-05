miesiac = input("Podaj miesiac")
dzien = int(input("Podaj dzien"))

# jeden z przykladow rozpisania warunkow
if miesiac == 'styczen' or miesiac == 'luty' or (miesiac == 'grudzien' and dzien >= 21) or (
    # linia byla dluzsza niz 120 znakow
    # linie mozemy lamac pod warunkiem ze uzyjemy nawiasow!!
        miesiac == 'marzec' and dzien < 21):
    print("zima")
elif miesiac == 'kwiecien' or miesiac == 'maj' or (miesiac == 'marzec' and dzien >= 21) or (
        miesiac == 'czerwiec' and dzien < 23):
    print('wiosna')
elif miesiac == 'lipiec' or miesiac == 'sierpien' or (miesiac == 'czerwiec' and dzien >= 23) or (
        miesiac == 'wrzesien' and dzien < 23):
    print('lato')
else:
    print('jesien')
