import tkinter
import waz


class Main(tkinter.Frame):
    CANVAS_WIDTH = 500
    CANVAS_HEIGHT = 500

    def __init__(self, root):
        super().__init__(root)

        self.canvas = tkinter.Canvas(self, width=self.CANVAS_WIDTH, height=self.CANVAS_HEIGHT)
        self.canvas.pack()

        self.przycisk = tkinter.Button(self, text="Resetuj", command=self.resetuj)
        self.przycisk.pack()

        self.jedzonko = waz.Punkt.losuj(self.CANVAS_WIDTH, self.CANVAS_HEIGHT)
        self.waz = waz.Waz.losuj(self.CANVAS_WIDTH, self.CANVAS_HEIGHT)

        self.__narysuj_punkt(self.jedzonko, 'red')
        self.__narysuj_punkt(self.waz, 'blue')
        self.zrob_krok()

    def __narysuj_punkt(self, punkt, kolor):
        self.canvas.create_rectangle(punkt.x, punkt.y, punkt.x, punkt.y, outline=kolor)

    def zrob_krok(self):
        if not self.jedzonko.czy_sie_nakladaja(self.waz):
            self.waz.zrob_krok(self.jedzonko)
            self.__narysuj_punkt(self.waz, 'blue')
            self.after(20, self.zrob_krok)

    def resetuj(self):
        self.canvas.delete('all')
        self.jedzonko = waz.Punkt.losuj(self.CANVAS_WIDTH, self.CANVAS_HEIGHT)
        self.__narysuj_punkt(self.jedzonko, 'red')
        self.waz = waz.Waz.losuj(self.CANVAS_WIDTH, self.CANVAS_HEIGHT)
        self.zrob_krok()

root = tkinter.Tk()
main = Main(root)
main.pack()
root.mainloop()
