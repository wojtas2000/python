# stworzmy klase Zagiel posiadajaca dwa atrybuty - powierzchnia (float) oraz material (string)
# stworzmy klase Jacht ktora posiada dwa atrybuty - "nazwa" (string) oraz "zagiel" (instancja klasy Zagiel)

class Zagiel:
    def __init__(self, powierzchnia, material):
        self.powierzchnia = powierzchnia
        self.material = material


class Jacht:
    def __init__(self, nazwa, zagiel):
        self.nazwa = nazwa
        self.zagiel = zagiel


jachcik = Jacht("Bar Młodzieży", Zagiel(25, "Dakron"))
print(jachcik.nazwa)
print(jachcik)
print(jachcik.zagiel.material)
