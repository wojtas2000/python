class Example(object):
    def __init__(self, parametry):
        self.parametry = parametry
        print("Podczas tworzenia nowego obiektu.")

    def __str__(self):
        return "To nasza super klasa z parametrem: {}".format(
            self.parametry
        )


example = Example("parametry")
print(example)
