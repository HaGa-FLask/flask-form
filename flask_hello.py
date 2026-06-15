import flask, markupsafe


flask_application = flask.Flask(__name__)


@flask_application.route('/')
def home():
    return '<h1>AMD Hackathlon deadline is Sunday 12 July 2026 </h1>'


#must include passing both parameter of methods=['POST', 'GET']) or Method Not Allowed for the requested url
@flask_application.route('/login', methods=['POST', 'GET'])
def login():
    if flask.request.method == 'POST':
        #username = flask.request.form.get('username')
        username = flask.request.form['username']
        return f'{username}'
    return flask.render_template('form.html')


#handles rendering the form
@flask_application.get('/login')
def login_form():
    return render_template('login.html')


#handles processing the submitted credentials
@flask_application.post('/login')
def login_process():
    username = request.form.get('username')
    #process authentication...
    return redirect(url_for('dashboard'))


@flask_application.route('/hello')
def hello():
    name = flask.request.args.get('name', default = 'default string name = HaGa')
    name = flask.request.args.get('name', 'Flask')
    return f'Hello, {markupsafe.escape(name)}!'
