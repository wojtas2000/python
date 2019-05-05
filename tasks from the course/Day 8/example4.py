liczba = input("Podaj liczbe: ")
try:
    liczba = int(liczba)
    print(10/liczba)
except ValueError:
    print("Musisz podac liczbe!")
    exit(1)
except ZeroDivisionError:
    print("Nie dziel przez zero")
    exit(1)
except Exception:
    print("Nieznany wyjatek")
    exit(1)
