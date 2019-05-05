# JSON
import json

with open('example.json') as plik:
    wczytany = json.load(plik)

print(wczytany)
print(type(wczytany))
print(wczytany["asd"])
print(type(wczytany["asd"]))
