# popraw te warunki, aby był tylko jeden poziom zagniezdzenia ifa

liczba = int(input("Podaj liczbe: "))

if liczba < 3:
    if liczba < 5:
        print('Liczba mniejsza od 3 i 5')
    else:
        print('Liczba mniejsza od 3 i wieksza badz rowna 5')
else:
    if liczba < 5:
        print("liczba wieksza badz rowna od 3 i mniejsza od 5")
    else:
        print('Liczba wieksza badz rowna 3 i wieksza badz rowna 5')
