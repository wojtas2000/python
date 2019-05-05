lista = [1, 2]

try:
    print("przed wyjatkiem")
    print(lista[4])  #4/0
    print("po wyjątku")
except IndexError:
    print("Nie ma takiego indeksu")
finally:
    print("Wykona sie zawsze")

print("Po try")
