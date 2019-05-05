import json

with open("weather.json") as plik:
    prognoza = json.load(plik)

print("Prognoza na Londyn")
print(prognoza["weather"][0]['description'])
