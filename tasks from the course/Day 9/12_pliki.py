uchwyt = open("sciezka/do/pliku")
uchwyt.close()  # po skonczonej pracy nalezy zamknac plik

with open("sciezka/do/pliku") as uchwyt:
    # jakies operacje do pliku
    pass

# uzywajac with plik zamykany jest po wykonaniu bloku kodu w with
