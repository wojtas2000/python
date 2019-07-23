# napisz program, ktory przyjmie od uzytkownika liczbe (float) i wypisze na ekran 10 podzielone przez ta liczbe.
# w przypadku, gdy uzytkownik nie poda liczby nalezy wypisac "Nalezy podac liczbę".
# w przypadku, gdy uzytkownik poda 0 nalezy wypisac "Pamietaj cholero, nie dziel przez zero!".
# Niezależnie czy użytkownik podał dobrą czy złą wartość na koniec należy wypisać "Dziękuję za współpracę".
# Nie używać ifów!

liczba = input("Podaj liczbe: ")
try:
    liczba = int(liczba)
    print(10/liczba)
except ValueError:
    print("Nalezy podac liczbę.")
except ZeroDivisionError:
    print("Pamietaj cholero, nie dziel przez zero!")
finally:
    print("Dziękuję za współpracę")
