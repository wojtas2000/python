import copy

lista1 = [[1, 2], [3, 4]]
lista2 = copy.deepcopy(lista1)
# gleboka kopia (kopiuje rowniez zagniezdzone listy)

lista1.append([5, 6])

lista2[0].append('a')
