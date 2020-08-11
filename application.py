from flask import Flask, render_template
import logging
from datetime import datetime
from random import randint
import requests
import json
from pprint import pprint

application = Flask(__name__, static_folder='static')

# set a 'SECRET_KEY' to enable the Flask session cookies
application.secret_key = 'random development key'


#
# @application.route('/random/number')
# def generate_random_number():
#     random_number = randint(0,100)
#     return {'random_number': '{}'.format(random_number)}
#
# @application.route('/random/string')
# def generate_random_string():
#     str_list = ['first','second','third']
#     position=randint(0,len(str_list)-1)
#     random_string = str_list[position]
#     return {'random_string': random_string}
#
# @application.route('/random/quote')
# def generate_random_quote():
#     quotes = [{'random_quote': 'Yeah we all shine on, like the moon, and the stars, and the sun.', 'quote_author': 'John Lennon'}, {'random_quote': 'I begin with an idea and then it becomes something else.', 'quote_author': 'Pablo Picasso'}, {'random_quote': 'Things do not change. We change.', 'quote_author': 'Henry David Thoreau'}, {'random_quote': 'If you take each challenge one step at a time, with faith in every footstep, your strength and understanding will increase.', 'quote_author': 'James Faust'}, {'random_quote': 'All I can say about life is, Oh God, enjoy it!', 'quote_author':'Bob Newhart'}, {'random_quote': 'A day of worry is more exhausting than a day of work.', 'quote_author':'John Lubbock'}]
#     #print(quotes)
#     #quote_api_endpoint = 'https://api.forismatic.com/api/1.0/?method=getQuote&lang=en&format=jsonp&jsonp=?'
#     #quote_api_endpoint = 'https://api.forismatic.com/api/1.0/?method=getQuote&lang=en&format=json'
#     #response = requests.get(quote_api_endpoint)
#     #pprint(response)
#     #if response.ok:
#     #    data = json.loads(response.content)
#     #    print(data)
#     #quote = response.json()['quoteText']
#     #author = response.json()['quoteAuthor']
#     #return {'random_quote': quote, 'quote_author': author}
#     position=randint(0,len(quotes)-1)
#     random_quote = quotes[position]
#     print(random_quote)
#     #quote=random_quote['random_quote']
#     #author=random_quote['quote_author']
#     return random_quote

@application.route('/home')
def home():
    return render_template('index.html')
    # This links the url /home to the navigation pane

@application.route('/game')
def game():
    return render_template('game.html')
    # This links the url /game to the start of the QSG

@application.route('/rules')
def rules():
    return render_template('rules.html')
    # This links the url /rules to help players understand the game

@application.route('/rulestoken')
def rulestoken():
    return render_template('rulestoken.html')
    # This links the url /rulestoken to understand types of tokens

@application.route('/rulescards')
def rulescards():
    return render_template('rulescards.html')
    # This links the url /rulescards to understand types of cards

@application.route('/rulespoints')
def rulespoints():
    return render_template('rulespoints.html')
    # This links the url /rulespoints to understand types of points that can be scored

@application.route('/contact')
def contact():
    return render_template('contact.html')
    # This links the url /contact to request for help and contact admin

@application.route('/user')
def user():
    return render_template('user.html')
    # This links the url /user to log in to a user profile instance

@application.route('/register')
def register():
    return render_template('register.html')
    # This links the url /register to create a user profile instance




# Mainline

if __name__ == '__main__':
    application.debug = True
    application.run()
