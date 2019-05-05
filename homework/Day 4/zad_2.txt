"""Zad 2.
Oblicz wiek psa z ludzkich lat.
W psich latach przez pierwsze dwa lata,
ka¿dy psi rok to 10,5 ludzkiego roku
kolejne lata, psi rok to 4 ludzkie lata
np. 15 ludzkich lat to 73 psie lata
"""

ile_lat = float(input("Podaj liczbê lat psa, a powiem Ci ile lat w przeliczeniu: "))

wiek = 0
lat_start = ile_lat

if 0 < lat_start <= 2:
    wiek = (ile_lat * 10.5)
    print("Twój pies ma: {} lat.".format(wiek))

elif lat_start > 2:
    wiek = 21
    ile_lat_po_2 = ile_lat - 2
    wiek += (ile_lat_po_2 * 4)

    print("Twój pies ma: {} lat.".format(int(wiek)))

else:
    print("Wprowadzi³es b³êdne dane.")

