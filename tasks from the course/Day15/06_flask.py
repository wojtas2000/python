import flask

app = flask.Flask("Testowa aplikacja :)")


@app.route('/<pin>')
def tajny(pin):
    if pin == '1234':
        return "ok"
    return 'Not ok', 403


app.run()