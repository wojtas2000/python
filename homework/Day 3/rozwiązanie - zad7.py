bok1 = int(input("Podaj bok A: "))
bok2 = int(input("Podaj bok B: "))
bok3 = int(input("Podaj bok C: "))

if (bok1 > bok2 + bok3
        or bok2 > bok1 + bok3
        or bok3 > bok1 + bok2):
# MUSIMY zaczac nawiasem warunek, zeby rozdzielic go na kilka lini
    print("nie prawidlowy trojkat")
else:
    if bok1 == bok2 == bok3:
        print("Trojkat rownoboczny")
    elif bok1 != bok2 and bok2 != bok3 and bok3 != bok1:
        print("Trojkat roznoboczny")
    else:
        # lub mozna zrobic
        # elif bok1 == bok2 or bok2 == bok3 or bok3 == bok1:
        # a roznoboczny w else
        print("Trojkat rownoramienny")
