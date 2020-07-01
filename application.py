from flask import Flask
import logging
from datetime import datetime
from random import randint

application = Flask(__name__, static_folder='simple-react/build', static_url_path='/')

# set a 'SECRET_KEY' to enable the Flask session cookies
application.secret_key = 'random development key'

# Routes
@application.route('/api/time')
def get_current_time():
    now = datetime.now() # current date and time

    return {'datetime': '{}'.format(now.strftime("%m/%d/%Y, %H:%M:%S"))}

@application.route('/random/number')
def generate_random_number():
    random_number = randint(0,100)
    return {'random_number': '{}'.format(random_number)}

@application.route('/')
def index():
    logging.warning('hello')
    return application.send_static_file('index.html')

#
# Mainline
#
if __name__ == '__main__':
    application.debug = False
    application.run()
