aktualny_rok = 2018

imie = input("Podaj imie")
rok = int(input("Podaj rok"))
wzrost = int(input("Podaj wzrost"))

print("Hello, {}! Masz juz {} lat i {}m.".format(
    imie, aktualny_rok - rok, wzrost/100
))
