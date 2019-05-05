"""
Zad 4.
Zgodnie z nową “Ustawą o rejestracji jachtów i innych jednostek pływających o długości do 24 m” obowiązkowi rejestracji podlegają jachty do długości od 7.5 metra. W przypadku poprzednich aktów prawnych było to 12 m. W obu ustawach krótsze jachty mogły być rejestrowane dobrowolnie.
Napisz program, który przyjmuje długość jachtu i wypisuje informację zgodne z nowym stanem prawnym:
Jacht nie podlega ustawie (powyzej 24 m)
Jacht podlegał obowiązkowej rejestracji i podlega ponownej rejestracji (powyzej 12m)
Jacht podlegał dobrowolnej rejestracji, będzie podlegał obowiązkowej rejestracji (powyzej 7.5m)
Jacht podlega dobrowolnej rejestracji (ponizej 7.5m)
"""

dlugosc_jachtu = float(input("Podaj dlugosc: "))

if dlugosc_jachtu > 24:
    print("Nie podlega ustawie")
elif dlugosc_jachtu > 12:
    print("Jacht podlegał obowiązkowej rejestracji i podlega ponownej rejestracji.")
elif dlugosc_jachtu > 7.5:
    print("Jacht podlegał dobrowolnej rejestracji, będzie podlegał obowiązkowej rejestracji.")
else:
    print("Jacht podlega dobrowolnej rejestracji.")
