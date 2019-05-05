def funkcja_zwracajaca_kilka():
    return "abc", 123


a, b = funkcja_zwracajaca_kilka()
krotka = funkcja_zwracajaca_kilka()

print(a, b)
print(krotka)
