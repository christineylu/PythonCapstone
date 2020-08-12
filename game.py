
'''Game play to link it together'''
class Game:
    def __init__(self, id):
        self.p1Went = False
        self.p2Went = False
        self.ready = False
        self.id = id
        self.moves = [None, None]
        self.wins = [0,0]
        self.ties = 0

    def get_player_move(self, p):
        """
        :param p: [0,1]
        :return: Move
        """
        return self.moves[p]

    def play(self, player, move):
        self.moves[player] = move
        if player == 0:
            self.p1Went = True
        else:
            self.p2Went = True

    def connected(self):
        return self.ready

    def allWent(self):
        return self.p1Went and self.p2Went

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

    def resetWent(self):
        self.p1Went = False
        self.p2Went = False

