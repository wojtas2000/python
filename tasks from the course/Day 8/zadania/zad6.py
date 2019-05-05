# popraw ten kod zgodnie z zasada "don't repeat yourself!" (nie powtarzaj kodu)


dzialanie = input("Wybierz dzialanie: (+,-,*,/)")

if dzialanie == '+':
    a = int(input('Podaj liczbe a: '))
    b = int(input('Podaj liczbe b: '))
    print(a+b)

elif dzialanie == '-':
    a = int(input('Podaj liczbe a: '))
    b = int(input('Podaj liczbe b: '))
    print(a-b)

elif dzialanie == '*':
    a = int(input('Podaj liczbe a: '))
    b = int(input('Podaj liczbe b: '))
    print(a*b)

elif dzialanie == '/':
    a = int(input('Podaj liczbe a: '))
    b = int(input('Podaj liczbe b: '))
    print(a/b)

else:
    print('Zly operator')