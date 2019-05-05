lista1 = [[1, 2], [3, 4]]
lista2 = lista1.copy()
# plytka kopia (kopiuje tylko liste zewnentrzna)

lista1.append([5, 6])

lista2[0].append('a')
