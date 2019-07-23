# otworz za pomoca pythona plik zad1.txt i utworz plik zad2a.txt zawierajacy ilosc znaków w pliku zad1.txt
# jak sprawdzic ile znakow ma plik polecam google :)

with open("zad1.txt") as plik:
    zawartosc = plik.read()
    dlugosc = len(zawartosc)

with open("zad2a.txt", "w") as plik:
    plik.write(str(dlugosc))  # write przyjmuje stringa wiec zmieniamy typ
