# napisz program sumujacy wszystkie elementy w podanej liscie (bez uzycia wbudowanej funkcji sum)
# (prawidlowy wynik to 50)

moja_lista = [1, 4, 7, 12, 12, 5, 9]

wynik = 0  # zmienna pomocnicza
for liczba in moja_lista:
    wynik += liczba

print(wynik)
print(sum(moja_lista))
