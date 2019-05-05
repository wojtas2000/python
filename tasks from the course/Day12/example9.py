class Kolo:
    def __init__(self, promien):
        self.promien = promien

    @classmethod
    def init_from_obwod(cls, obwod):
        promien = obwod/(3.14*2)
        return cls(promien)


a = Kolo(100 / (3.14*2))
b = Kolo.init_from_obwod(100)
