from flask import Flask, render_template
import tkinter as tk


root = tk.Tk()
root.title("Click me!")
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

'''Tying value to cards for ranking'''
class Card(object):
    FACES = {10: 'Jack', 11: 'Queen', 12: 'King', 13: 'Ace', 14: 'Goat'}

    def __init__(self, rank, suit):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        value = self.FACES.get(self.rank, self.rank)
        return "{0} of {1}".format(value, self.suit)

    def __lt__(self, other):
        return self.rank < other.rank


'''Associating the cards with different sneaker types'''
import random
class Collection(object):
    def __init__(self, ranks=None, suits=None):
        if ranks is None:
            ranks = range(2, 15)
        if suits is None:
            suits = ['Fire', 'Diamond', 'Money', 'Hundred']
        self.deck = []
        for r in ranks:
            for s in suits:
                self.deck.append(Card(r, s))

    def deal(self, n):
        random.shuffle(Card)
        return random.sample(self.deck, n)

# '''Associate image dictionary to each card value type'''
# def create_images_Money():
#     """create all card images as a card_name:image_object dictionary"""
#     Collection = Card(:15)
#     image_dict = {}
#     for card in Collection:
#         # all images have filenames that match the card_list names + extension .gif
#         image_dict[card] = tk.PhotoImage(file=image_dir+card+".gif")
#         #print image_dir+card+".gif"  # test
#     return image_dict
# image_dir = "/Users/christinelu/Desktop/nyu_capstone/aws_elastic_beanstalk_flask/PythonCapstone/static/Money"
## def create_images_Diamond():
#     """create all card images as a card_name:image_object dictionary"""
#     Collection = Card(:15)
#     image_dict = {}
#     for card in Collection:
#         # all images have filenames that match the card_list names + extension .gif
#         image_dict[card] = tk.PhotoImage(file=image_dir+card+".gif")
#         #print image_dir+card+".gif"  # test
#     return image_dict
# image_dir = "/Users/christinelu/Desktop/nyu_capstone/aws_elastic_beanstalk_flask/PythonCapstone/static/Diamond"
# '''Segmenting the images to the suit of card'''
## def create_images_100():
#     """create all card images as a card_name:image_object dictionary"""
#     Collection = Card(:15)
#     image_dict = {}
#     for card in Collection:
#         # all images have filenames that match the card_list names + extension .gif
#         image_dict[card] = tk.PhotoImage(file=image_dir+card+".gif")
#         #print image_dir+card+".gif"  # test
#     return image_dict
# image_dir = "/Users/christinelu/Desktop/nyu_capstone/aws_elastic_beanstalk_flask/PythonCapstone/static/100"
## def create_images_Fire():
#     """create all card images as a card_name:image_object dictionary"""
#     Collection = Card(:15)
#     image_dict = {}
#     for card in Collection:
#         # all images have filenames that match the card_list names + extension .gif
#         image_dict[card] = tk.PhotoImage(file=image_dir+card+".gif")
#         #print image_dir+card+".gif"  # test
#     return image_dict
# image_dir = "/Users/christinelu/Desktop/nyu_capstone/aws_elastic_beanstalk_flask/PythonCapstone/static/Fire"
# '''load all card images into a dictionary'''
# image_dict = create_images_Money()
# image_dict.update(create_images_Diamond())
# image_dict.update(create_images_Fire())
# image_dict.update(create_images_100())
# #test output
# print image_dict
# '''making a canvas to upload images'''
# width1 = 5 * photo1.width() + 100
# height1 = photo1.height() + 20
# canvas1 = tk.Canvas(width=width1, height=height1)
# canvas1.pack()
# '''Run Tinker'''
# root.mainloop()
# # Mainline

if __name__ == '__main__':
    application.debug = True
    application.run()
