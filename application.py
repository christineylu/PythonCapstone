from flask import Flask
import logging
from datetime import datetime
from random import randint
import requests
import json
from pprint import pprint

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

@application.route('/random/string')
def generate_random_string():
    str_list = ['first','second','third']
    position=randint(0,len(str_list)-1)
    random_string = str_list[position]
    return {'random_string': random_string}

@application.route('/random/quote')
def generate_random_quote():
    #quote_api_endpoint = 'https://api.forismatic.com/api/1.0/?method=getQuote&lang=en&format=jsonp&jsonp=?'
    quote_api_endpoint = 'https://api.forismatic.com/api/1.0/?method=getQuote&lang=en&format=json'
    response = requests.get(quote_api_endpoint)
    pprint(response)
    if response.ok:
        data = json.loads(response.content)
        print(data)
    quote = response.json()['quoteText']
    author = response.json()['quoteAuthor']
    return {'random_quote': quote, 'quote_author': author}


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
