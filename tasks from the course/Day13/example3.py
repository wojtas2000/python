import sys

if len(sys.argv) != 3:
    print("Zla ilosc argumentow!")
    exit(1)
# jest tez bibliotka argparse to ladniejszego parsowania argumentow
# jest jeszcze click (ja nalezy zainstalowac pipem)

liczba = int(sys.argv[1])
napis = sys.argv[2]

print(liczba * napis)

zmienna = "a" if True else "b"
