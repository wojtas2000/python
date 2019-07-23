# 1) skopiuj podana liste do zmiennej "moja_lista_copy"
# 2) przypisz referencje "moja_lista" do zmiennej "moja_lista2" (nie kopie!)
# 3) dodaj nowy element "x" do "moja_lista"
# 3) dodaj nowy element "y" do "moja_lista_copy"
# 4) wypisz zawartosc "moja_lista", "moja_lista2", "moja_lista_copy"

moja_lista = ['a', 'b', 'c']

moja_lista_copy = moja_lista.copy()
moja_lista2 = moja_lista

moja_lista.append("x")
moja_lista_copy.append("y")

print("moja_lista", moja_lista)
print("moja_lista2", moja_lista2)
print("moja_lista_copy", moja_lista_copy)

