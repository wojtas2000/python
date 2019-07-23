# Napisz testy do klasy Kolo z pliku 'kolo.py'. Pamiętaj o przetestowaniu wszystkich możliwych sposobów interakcji
# oraz przypadki brzegowe.

import unittest
from kolo import Kolo


class KoloTests(unittest.TestCase):
    def test_czy_rzuca_blad_na_litere(self):
        with self.assertRaises(ValueError):
            k = Kolo('a')

    def test_kolo_z_ujemna(self):
        with self.assertRaises(ValueError):
            k = Kolo(-12)

    def test_kolo_is_ok(self):
        k = Kolo(10)
        self.assertEqual(
            10,
            k.promien
        )
        self.assertEqual(
            20,
            k.srednica
        )

    def test_zmiana_srednicy(self):
        k = Kolo(10)
        k.srednica = 30
        self.assertEqual(
            30,
            k.srednica
        )
        self.assertEqual(
            15,
            k.promien
        )

    def test_zmiana_promienia(self):
        k = Kolo(10)
        k.promien = 30
        self.assertEqual(
            60,
            k.srednica
        )
        self.assertEqual(
            30,
            k.promien
        )

    def test_zmiana_promienia_na_ujemna(self):
        k = Kolo(12)
        with self.assertRaises(ValueError):
            k.promien = -12

    def test_zmiana_srednica_na_ujemna(self):
        k = Kolo(12)
        with self.assertRaises(ValueError):
            k.srednica = -12
