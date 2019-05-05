# Zad 2.
# Program przyjmuje liczbe i wypisuje “Wspaniala liczba milordzie!” jesli liczba jest w zakresie 5 < x < 12, gdy jest mniejsza od 5 “Za malo!”, gdy wieksza o 12 “Za duzo!”

liczba = input("Podaj liczbe: ")
liczba = int(liczba)

if 5 < liczba < 12:
    print("Wspaniala liczba, milordzie!")
elif liczba <= 5:
    print("Za malo!")
else:  # nie podaje tutaj warunku bo juz wiem, ze liczba jest wieksza niz 12
    print("Za duzo!")
