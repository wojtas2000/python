with open("00_teoria.txt", encoding="utf-8") as uchwyt:
    print(uchwyt.read())  # caly plik na raz

with open("00_teoria.txt", encoding="utf-8") as uchwyt:
    print(uchwyt.readlines())  # lista stringow

with open("00_teoria.txt", encoding="utf-8") as uchwyt:
    linia = uchwyt.readline()
    while linia:
        print(linia)
        # w pamięci jest przechowywana tylko jedna linia
        linia = uchwyt.readline()
