# przyjmij od uzytkownika liczbe i utworz plik zad3.txt zawierajaca kolejne potegi dwójki w kazdej lini az do podanej liczby
# czyli np. dla 5 plik wynikowy powinien wygladac:
# 2
# 4
# 8
# 16
# 32

potega = int(input("Podaj liczbe: "))

with open("zad3.txt", "w") as plik:
    for wykladnik in range(0, potega + 1):
        plik.write(str(2**wykladnik))
        plik.write("\n")
