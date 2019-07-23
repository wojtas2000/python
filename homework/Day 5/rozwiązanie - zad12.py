# napisz program ktory wygeneruje zagniezdzona 100 razy liste z elementem 'a'

# tworzymy najbardziej wewnentrzna liste
outer = ['a']

for x in range(99):  # jedna liste juz mamy :)
    # tworzymy nowa liste, zawierajaca stara zewnentrzna i przypisujemy do tej samej zmiennej
    outer = [outer]


# polecam odpalic ten kod w pythontutorze
print(outer)
