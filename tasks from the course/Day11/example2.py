class WalutaZloty:
    def __init__(self, zlote, grosze):
        self.zlote = zlote
        self.grosze = grosze

    def __add__(self, other):
        zlote = self.zlote + other.zlote
        grosze = self.grosze + other.grosze

        pelne_zlotowki = grosze // 100
        zlote += pelne_zlotowki
        grosze -= (pelne_zlotowki * 100)

        return WalutaZloty(zlote, grosze)

    def __str__(self):
        return "{} zl i {} gr".format(self.zlote, self.grosze)

    def __eq__(self, other):
        if not isinstance(other, WalutaZloty):
            return False
        return self.grosze == other.grosze and self.zlote == other.zlote


wartosc1 = WalutaZloty(1, 23)
wartosc2 = WalutaZloty(3, 99)

wartosc3 = wartosc1 + wartosc2
print(wartosc3)
wartosc4 = WalutaZloty(5, 22)

print(wartosc3 == wartosc1)
print(wartosc4 == wartosc3)
print("string" == 12)
print("string" == wartosc4)
#print(wartosc4 == "to jest string")
