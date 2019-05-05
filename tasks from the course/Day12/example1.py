class Horse(object):
    def czym_jestem(self):
        print("Kon")


class Donkey(object):
    def czym_jestem(self):
        print("Osiol")


class Mule(Horse, Donkey):
    pass


m = Mule()
print(isinstance(m, Horse))
print(isinstance(m, Donkey))
m.czym_jestem()

print(Mule.mro())  # funkcja mro() zwraca kolejnosc w jakies python szuka metod
