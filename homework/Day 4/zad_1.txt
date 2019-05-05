"""Zad 1.
Narysuj piramidê Mario - jako input - wysokoœæ piramidy
np. piramida wysokoœci 3 ma wygl¹daæ:

  #
 ###
#####

"""

wysokosc = int(input("Wpisz wysokoœæ piramidy: "))

y = 2

for i in range(wysokosc, 0, -1):
    print((" " * (i - 1)) + ("#" * (y - 1)))
    y += 2

