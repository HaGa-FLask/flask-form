import flask

flask_application = flask.Flask(__name__)

@flask_application.route('/')
def hello():
    return '<h1>AMD Hackathlon deadline is Sunday 12 July 2026 </h1>'

#must include passing both parameter of methods=['POST', 'GET']) or Method Not Allowed for the requested url
@flask_application.route('/login', methods=['POST', 'GET'])
def login():
    if flask.request.method == 'POST':
        #username = flask.request.form.get('username')
        username = flask.request.form['username']
        return f'{username}'
    return flask.render_template('form.html')
