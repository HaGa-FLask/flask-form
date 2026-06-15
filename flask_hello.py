import flask, markupsafe


flask_application = flask.Flask(__name__)


@flask_application.route('/')
def index():
    #http://example.com/admin/login
    return flask.redirect('login')
    return flask.redirect(flask.url_for('login'))


@flask_application.route('/')
def index2():
    return 'index'


@flask_application.route('/')
def home():
    return '<h1>AMD Hackathlon deadline is Sunday 12 July 2026 </h1>'


#must include passing both parameter of methods=['POST', 'GET']) or Method Not Allowed for the requested url
#because the default is @flask_application.route('/login', methods=['GET'])
@flask_application.route('/login', methods=['POST', 'GET'])
def login():
    if flask.request.method == 'POST':
        #username = flask.request.form.get('username')
        username = flask.request.form['username']
        return f'{username}'
    return flask.render_template('form.html')


@flask_application.route('/login')




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
@flask_application.route('/hello/<name>')
def hello(name=None):
    return flask.render_template('hello.html', person=name)


@flask_application.route('/hello')
def hello2():
    name = flask.request.args.get('name', default = 'default string name = HaGa')
    name = flask.request.args.get('name', 'Flask')
    return f'Hello, {markupsafe.escape(name)} !'


#ValueError: URL rule 'user' must start with a slash.
@flask_application.route('/user/<username>')
#TypeError: show_user_profile() missing 1 required positional argument: 'username'
def show_user_profile(username):
    #SyntaxError: f-string: valid expression required before '}'
    return f'this is user {username} profile page.'


@flask_application.route('/post/<int:post_id>')
def show_post(post_id):
    return f'post_id number {post_id}.'


with flask_application.test_request_context():
    print(flask.url_for('index'))


with flask_application.test_request_context('/hello', method='POST'):
    assert flask.request.path == '/hello'

































