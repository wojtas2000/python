wartosc_boolowska = True

if wartosc_boolowska:
    print("Jesli prawda")
else:
    print("Jesli nieprawda")

wartosc_boolowska1 = False
wartosc_boolowska2 = True

if wartosc_boolowska1:
    # if musi byc jeden
    print("jesli 1 prawda")
elif wartosc_boolowska2:
    # moze byc nieograniczona ilosc elifow, ale wykona sie conajwyzej 1
    print("jesli 2 prawda")
else:
    # moze byc tylko jeden else, ale nie musi
    print("Jesli nieprawda")
