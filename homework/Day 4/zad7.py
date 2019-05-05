"""
Napisz program ktory przyjmuje napis i wyswietla liczbe liter oraz cyfr w podanym napisie.
https://docs.python.org/3/library/stdtypes.html#string-methods
"""

napis = input("Podaj napis: ")

liczba_liter = 0
liczba_cyfr = 0

for znak in napis:
    if znak.isdigit():  # czy napis sklada sie wylacznie z cyfr
        liczba_cyfr = liczba_cyfr + 1
    elif znak.isalpha():
        liczba_liter = liczba_liter + 1

print("Twoj napis zawiera {} cyfr i {} liter".format(
    liczba_cyfr, liczba_liter
))
