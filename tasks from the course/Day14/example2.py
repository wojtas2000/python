import json

slownik = {}

for x in range(0, 100):
    slownik[x] = x

print(slownik)
zjsonowany = json.dumps(slownik)
print(type(slownik))
print(zjsonowany)
print(type(zjsonowany))

slownik2 = json.loads(zjsonowany)
print(slownik2)
print(type(slownik2))
