class Samochod:
    def __init__(self, marka):
        self.marka = marka
        self.czy_wlaczony = False

    def wlacz(self):
        self.czy_wlaczony = True

    def wylacz(self):
        self.czy_wlaczony = False


samochod = Samochod("Volvo")
# samochod.czy_wlaczony = True
samochod.wlacz()
