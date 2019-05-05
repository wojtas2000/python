with open("example.txt") as plik:
    linia = plik.readline()
    print(linia)
    linia = plik.readline()  # kazde kolejne wywolanie daje kolejna linie
    print(linia)
    linia = plik.readline()
    print(linia)
    linia = plik.readline()  # tu juz nie ma wiecej lini, zwraca pusty string
    print(linia)
