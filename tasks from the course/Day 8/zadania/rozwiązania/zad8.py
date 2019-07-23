# znajdz blad w funkcji! funkcja powinna przyjmowac liste i dodac do niej 1, lub zwrocic liste z sama jednynka
# jesli nie poda sie nic, ale jednak robi cos innego...


def foo(bar=[]):
    bar.append(1)
    return bar


print(foo([1]))  # [1, 1] tu sie wynik zgadza
print(foo([]))  # [1] tu tez
print(foo())  # [1] i tu!
print(foo())  # [1, 1] oj cos jest nie tak
print(foo())  # [1, 1, 1] zatrzymajcie ta karuzele bledu!
