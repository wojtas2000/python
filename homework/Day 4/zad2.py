"""
Dla kazdej litery w napisie podanym przez uzytkownika wypisz jej kod ASCII
"""
napis = input("Podaj napis: ")

for litera in napis:
    print(ord(litera))
