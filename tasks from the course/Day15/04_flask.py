import flask
import wiringpi

app = flask.Flask("GPIO")


@app.route('/zgas')
def zgas():
    wiringpi.digitalWrite(6, 0)
    return "Zgaszono!"


@app.route('/zapal')
def zapal():
    wiringpi.digitalWrite(6, 1)
    return "Zapalono!"


wiringpi.wiringPiSetupGpio()
wiringpi.pinMode(6, 1)       # Set pin 6 to 1 ( OUTPUT )
app.run()
