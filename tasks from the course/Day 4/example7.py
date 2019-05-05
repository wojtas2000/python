# uzytkownik podaje liczby az poda 77

liczba = int(input("Podaj liczbe: "))

while liczba != 77: # petla wykonuje sie dopoki uzytkownik nie poda 77
    print("Zla liczba!")
    liczba = int(input("Podaj liczbe: "))

print("Dobra liczba!")
