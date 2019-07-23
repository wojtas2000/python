"""
Zad 5.
Po podaniu ilości punktów podaj ocenę na podstawie progu procentowego:

5 od 90%, 4+ od 80, 4 od 70, 3+ od 60, 3 od 50
"""
pkt = int(input("Podaj ilosc punktow"))

if pkt >= 90:
    print("5")
elif pkt >= 80:
    print("4+")
elif pkt >= 70:
    print("3")
elif pkt >= 60:
    print("3+")
elif pkt >= 50:
    print("3")
else:
    print("2")
