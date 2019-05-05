# wypisz liczby od 1 do 100 (wlacznie)
# jesli podzielna przez 3 to napisz Fizz
# jesli podzilena przez 5 to napisz Buzz
# jesli podzielna przez 3 i przez 5 to napisz FizzBuzz

for liczba in range(1, 101):  # musimy podac o 1 wieksza niz ostatnia
    if liczba % 3 == 0:
        print("Fizz", end='')
        if liczba % 5 != 0:
            print()
    if liczba % 5 == 0:
        print("Buzz")
