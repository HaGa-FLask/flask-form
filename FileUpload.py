import flask

flaskApp = flask.Flask(__name__)

@flaskApp.route('/')
def main():
    return flask.render_template('index.html')
