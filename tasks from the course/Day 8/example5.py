def funkcja(a):
    if a % 2 != 0:
        raise ValueError("Chce parzysta!")
    return a * 2


try:
    funkcja(3)
except ValueError:
    print("Funkcja rzucila blad")
