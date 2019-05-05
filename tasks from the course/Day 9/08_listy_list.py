lista_listy = [
    [1, 2, 3],
    [4, 5, 6],
]
print(lista_listy[0][1])

plytka_kopia = lista_listy.copy()
plytka_kopia[0].append("nowy")

print(lista_listy)
import copy

gleboka_kopia = copy.deepcopy(lista_listy)
gleboka_kopia[0].append("w kopii")
print(lista_listy)
