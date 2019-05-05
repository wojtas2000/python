import flask

app = flask.Flask("Testowa aplikacja :)")


@app.route('/')
def hello_world():
    return "Hello, world!"


@app.route('/test')
def test():
    return "test"


app.run()
