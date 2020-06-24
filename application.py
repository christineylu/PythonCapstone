from flask import Flask
from flask import url_for
from markupsafe import escape
from flask_debugtoolbar import DebugToolbarExtension
import logging
from jinja2 import Environment, PackageLoader, select_autoescape

application = Flask(__name__)

# set a 'SECRET_KEY' to enable the Flask session cookies
application.secret_key = 'random development key'

toolbar = DebugToolbarExtension(application)

# Set up jinja2 templating
env = Environment(
    loader=PackageLoader(__name__, 'templates'),
    autoescape=select_autoescape(['html', 'xml'])
)


# Routes
@application.route('/')
def index():
    logging.warning("See this message in Flask Debug Toolbar!")
    template = env.get_template('index.html')
    title='title = {}'.format(__name__)
    page_name='INDEX PAGE'
    name = 'Ronald'
    return template.render(title=title, page_name=page_name, name=name)

@application.route('/hello')
def hello():
    return "<html><body>HELLO PAGE<p>Hello, <b>World</b>!<p> You're in the hello page.</body></html>"

@application.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    #return 'User %s' % escape(username)
    template = env.get_template('username.html')
    title='title = {}'.format(username)
    page_name='USER PAGE'
    return template.render(title=title, page_name=page_name, username=username)

@application.route('/post/number/<int:post_id>')
def show_post_number(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@application.route('/post/string/<string:post_str>')
def show_post_letter(post_str):
    # show the post with the given string, the id is a string
    return 'Post %s' % post_str

@application.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % escape(subpath)

# with app.test_request_context():
#     print(url_for('index'))
#     print(url_for('login'))
#     print(url_for('login', next='/'))
#     print(url_for('profile', username='John Doe'))

#
# Mainline
#
if __name__ == '__main__':
    application.run()
