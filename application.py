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
