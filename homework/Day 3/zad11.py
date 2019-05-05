liczba_a = float(input('Podaj liczbe a: '))
liczba_b = float(input('Podaj liczbe b: '))
znak = input('Podaj dzialanie (+, -, *, /): ')

wynik = None
if znak == '*':
    wynik = liczba_a * liczba_b
elif znak == '+':
    wynik = liczba_a + liczba_b
elif znak == '-':
    wynik = liczba_a - liczba_b
elif znak == '/':
    if liczba_b == 0:
        print('DZIELENIE PRZEZ ZERO')
        print("https://bit.ly/2HykpKn")
        exit(1)
        # do exit podajemy exit_code
        # przyjmuje sie ze exit_code rozny od 0 to blad
        # python w przypadku skonczenia skryptu bez bledu zwraca 0
    wynik = liczba_a/liczba_b
else:
    print('Nieznany znak :(')
    exit(1)


print("{} {} {} = {}".format(liczba_a, znak, liczba_b, wynik))