import requests


for x in range(0, 10000):
    url = 'http://127.0.0.1:5000/{:04}'.format(x)
    response = requests.get(url)
    if response.status_code == 200:
        print("pin to: {:04}".format(x))
        break
