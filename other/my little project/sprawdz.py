def czy_poprawnie(imie, nazwisko):
    wynik = 0
    for char in (imie+nazwisko):
        if char.isalpha():
            wynik += 1

            if wynik == len(imie+nazwisko):
                return True
        else:
            print("Niepoprawnie wprowadzone dane.\n")
            break




