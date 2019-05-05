import unittest


class Matematyka:
    def dodaj(self, a, b):
        return a + b


class MatematykaTests(unittest.TestCase):
    def setUp(self):
        print("Wykonuje sie przed kazdym testem")
        self.instancja = Matematyka()

    def tearDown(self):
        print("Wykonuje sie po kazdym tescie")
        self.instancja = None

    def test_czy_dodaje(self):
        wynik = self.instancja.dodaj(12, 45)
        self.assertEqual(57, wynik)

    def test_czy_dodaje_zero(self):
        wynik = self.instancja.dodaj(12, 0)
        self.assertEqual(12, wynik)

    def test_czy_dodaje_ujemna(self):
        wynik = self.instancja.dodaj(12, -12)
        self.assertEqual(0, wynik)
