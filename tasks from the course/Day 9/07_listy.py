lista = ["a", "b", "c"]

print(lista[0])

lista[1] = "d"
print(lista)

lista.append("f")

del lista[2]
print(lista)

# print(lista[4])   # rzuci blad - wyszlismy poza zasieg listy

lista2 = lista
lista.append("t")

print(lista2)

lista3 = lista.copy()
lista.append("x")

print(lista3)
