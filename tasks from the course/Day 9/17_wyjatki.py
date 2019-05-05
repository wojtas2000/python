try:
    lista = []
    print(lista[0])
except (IndexError, KeyError):
    print("Nie ma tego elementu na liscie")
except ValueError:
    print("Obsluga value error")

try:
    12/0  # wyjatek dzielenia przez 0 nie zostanie zlapany i wywali program
except IndexError:
    print("obsluga index error")
