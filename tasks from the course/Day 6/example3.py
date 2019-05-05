def funkcja_z_opcjonalnym(a, b=12, c=10):
    print("Zawolano z argumentami:", a, b, c)


funkcja_z_opcjonalnym(5)
funkcja_z_opcjonalnym(5, "abc", 90)
funkcja_z_opcjonalnym(5, c=20)
