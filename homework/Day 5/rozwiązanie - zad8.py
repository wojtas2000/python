# przyjmuj od uzytkownika kolejne napisy tak dlugo az wpisze on "KONIEC"
# dodawaj kolejne wpisane napisy do listy
# wypisz na koniec liste wszystkich napisow

napis = 'TEN NAPIS JEST GLUPI PO TO ZEBY PETLA PRZESZLA RAZ'
napisy = []

while napis != 'KONIEC':
    napis = input("Podaj napis: ")
    napisy.append(napis)

print("Wpisałeś: ")
print(napisy)
