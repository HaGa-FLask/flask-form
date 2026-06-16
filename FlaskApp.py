import flask
import markupsafe


flaskApp = flask.Flask(__name__)


@flaskApp.route('/')
def main():
    return flask.render_template('index.html')


@flaskApp.route('/')
def index():
    #http://example.com/admin/login
    return flask.redirect('login')
    return flask.redirect(flask.url_for('login'))


@flaskApp.route('/')
def index2():
    return 'index'


@flaskApp.route('/')
def index3():
    return 'index', 500


@flaskApp.route('/')
def home():
    return '<h1>AMD Hackathlon deadline is Sunday 12 July 2026 </h1>'


#must include passing both parameter of methods=['POST', 'GET']) or Method Not Allowed for the requested url
#because the default is @flaskApp.route('/login', methods=['GET'])
@flaskApp.route('/login', methods=['POST', 'GET'])
def login():
    if flask.request.method == 'POST':
        #username = flask.request.form.get('username')
        username = flask.request.form['username']
        return f'{username}'
    return flask.render_template('form.html')


@flaskApp.route('/login')
def login_abort_http_401():
    #http 401 unauthorized error means your request failed because it lacks valid authentication credentials
    flask.abort(401)
    what()()


#handles rendering the form
@flaskApp.get('/login')
def login_form():
    return flask.render_template('login.html')


#handles processing the submitted credentials
@flaskApp.post('/login')
def login_process():
    username = flask.request.form.get('username')
    #process authentication...
    return flask.redirect(flask.url_for('dashboard'))


@flaskApp.route('/hello')
@flaskApp.route('/hello/<name>')
def hello(name=None):
    return flask.render_template('hello.html', person=name)


@flaskApp.route('/hello')
def hello2():
    name = flask.request.args.get('name', default='default string name = HaGa')
    name = flask.request.args.get('name', 'Flask')
    return f'Hello, {markupsafe.escape(name)} !'


#ValueError: URL rule 'user' must start with a slash.
@flaskApp.route('/user/<username>')
#TypeError: show_user_profile() missing 1 required positional argument: 'username'
def show_user_profile(username):
    # SyntaxError: f-string: valid expression required before '}'
    return f'this is user {username} profile page.'


@flaskApp.route('/post/<int:post_id>')
def show_post(post_id):
    return f'post_id number {post_id}.'


with flaskApp.test_request_context():
    print(flask.url_for('index'))


with flaskApp.test_request_context('/hello', method='POST'):
    assert flask.request.path == '/hello'


@flaskApp.errorhandler(404)
def page_not_found(error):
    #without return 404, flask would return status code 200 OK, which is incorrect because the page was not found
    return flask.render_template('page_not_found.html'), 404


if __name__ == '__main__':
    flaskApp.run(debug=True)
