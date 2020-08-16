from flask import Flask, render_template
from tkinter import *
import tkinter as tk
import random
import pygame
from graphics import *

application = Flask(__name__, static_folder='static')
application.secret_key = 'random development key'

'''Flask Kick off link not working - go directly to:''' # http://127.0.0.1:5000/home

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
'''taken out of MVP'''
# @application.route('/rulestoken')
# def rulestoken():
#     return render_template('rulestoken.html')
#     # This links the url /rulestoken to understand types of tokens
# @application.route('/user')
# def user():
#     return render_template('user.html')
#     # This links the url /user to log in to a user profile instance
# @application.route('/register')
# def register():
#     return render_template('register.html')
#     # This links the url /register to create a user profile instance
#
'''Tying value to cards for ranking'''
# class Card(object):
#     # # Omitting face card ranking for MVP
#     # FACES = {11: '100', 12: 'Diamond', 13: 'Fire', 14: 'Money'}
#     def __init__(self, rank, suit):
#         self.suit = suit
#         self.rank = rank
#
#     def __str__(self):
#         # # Omitting face card ranking for MVP
#         # value = self.FACES.get(self.rank, self.rank)
#         return "{0}_{1}".format(self.rank, self.suit)
#
#     def __lt__(self, other):
#         return self.rank < other.rank

'''Associating the cards with different sneaker types'''
# import random
# class Collection(object):
#     def __init__(self, rank, suits=None):
#         if suits is None:
#             suits = ['FYE', 'DMD', 'MNY', '100']
#         self.deck = []
#         for r in rank:
#             for s in suits:
#                 self.deck.append((r,s))
#
#     def deal(self, n):
#         random.shuffle(Card)
#         return random.sample(self.deck, n)

'''Attempted to use class to loop through image dictionary to associate to card - unsuccessful'''
# # class SneakerCards(object):
# def Image_Load():
#         # image_dict = {}
#     for suit in self.suits:
#         for number in self.rank:
#             card_name = f"{suit}_{number}"
#             folder_name = f"pygame.image.load('static/{suits}/{card_name}.png')"
#             image_dict[card_name] = folder_name
# # test output
# print(Image_Load)
'''Attempted to loop through image dictionary to each suit type - unsuccessful'''
# def images(self):
#     image_dict = {}
#     for suit in self.suits:
#         for number in self.rank:
#             card_name = f"{suit}_{number}"
#             folder_name = f"pygame.image.load('static/{suit}/{card_name}.png')"
#             image_dict[card_name] = folder_name
#     return image_dict
'''Pivoted to TKinter in attempt to bypass Flask's broken HTML link'''
root = tk.Tk()
root.title("QUARANTINE SNEAKER GAME")
'''Set TKinter background for game play'''


'''Set up winner'''
def winner(self):
    p1 = self.moves[0].upper()[0]
    p2 = self.moves[1].upper()[0]

    winner = -1
    if p1 == "Fire" and p2 == "Money":
        winner = 0
    elif p1 == "Money" and p2 == "Fire":
        winner = 1
    elif p1 == "Diamond" and p2 == "Fire":
        winner = 0
    elif p1 == "Fire" and p2 == "Diamond":
        winner = 1
    elif p1 == "Money" and p2 == "Diamond":
        winner = 0
    elif p1 == "Diamond" and p2 == "Money":
        winner = 1

    return winner

'''Set up graphics for play'''
def create_cards():
    suits = ['FYE', 'DMD', 'MNY', '100']
    return [suit + "_" + rank for suit in suits for rank in "A23456789TJQK" ]

card_list = create_cards()

def shuffle_cards(card_list):
    """random shuffle a list of cards"""
    # make a copy of the original list
    card_list1 = card_list[:]
    random.shuffle(card_list1)
    return card_list1

def pick_5cards(card_list):
    """pick five cards from the shuffled list"""
    return card_list[:5]

image_dir = "/Users/christinelu/Desktop/nyu_capstone/aws_elastic_beanstalk_flask/PythonCapstone/static/"
# IMAGE PATH NAME: /Users/christinelu/Desktop/nyu_capstone/aws_elastic_beanstalk_flask/static/FYE_A.gif

def create_images():
    """create all card images as a card_name:image_object dictionary"""
    card_list = create_cards()
    image_dict = {}
    for card in card_list:
        # all images have filenames that match the card_list names + extension .gif
        image_dict[card] = tk.PhotoImage(file=image_dir+card+".gif")
        '''How does TKinter ingest images??? - find out'''
        # print (image_dir+card)  # test
    return image_dict

def next_hand(event):
    """create the card list, shuffle, pick five cards and display them"""
    card_list = create_cards()
    card_list = shuffle_cards(card_list)
    card_list = pick_5cards(card_list)
    root.title(card_list)  # test
    '''Positioning the cards on the game board'''
    x = 10
    y = 10
    for card in card_list:
        #print card, x, y  # test
        canvas1.create_image(x, y, image=image_dict[card], anchor='nw')
        # calculate each NW corner x, y
        x += 90

image_dir = "/Users/christinelu/Desktop/nyu_capstone/aws_elastic_beanstalk_flask/PythonCapstone/static/"


# photo1 = tk.PhotoImage(file=image_dir+str(create_cards())+".jpg")
'''Expanding the window to fit game play'''
# width1 = 5 * photo1.width() + 100
# height1 = photo1.height() + 20
# canvas1 = tk.Canvas(width=width1, height=height1)
# canvas1.pack()

'''Entering images into dictionary'''
image_dict = create_images()
'''Mouse binding to window'''
canvas1.bind('<Button-1>', next_hand)
'''Kick off QSG!'''
root.mainloop()

'''Test'''
print (card_list)
print(image_dict)

# # Mainline
if __name__ == '__main__':
    application.debug = True
    application.run()
