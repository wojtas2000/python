# napisz program ktory podzieli napis 'ala ma kota' na liste slow
# nastepnie zamieni pierwsze slowo z ostatnim i polaczy z powrotem w napis uzywajac _ zamiast spacji

slowa = 'ala ma kota'.split()  # split dzieli string po podanym znaku, jak nie podamy zadnego to dzieli po spacji
# czyli dzieli na slowa

# zamieniamy miejscami pierwsze z ostatnimi
pomocnicza = slowa[0]
slowa[0] = slowa[-1]
slowa[-1] = pomocnicza

# lub bez zmiennej pomocniczej:
# slowa[0], slowa[-1] = slowa[-1], slowa[0]
# w pythonie mozemy w jednym kroku przypisac kilka zmiennych naraz

# join laczy podana liste w jeden string odzielajac elementy stringiem na ktorym zostal wywolany
wynik = '_'.join(slowa)

print(wynik)