import copy
import random

from persistent import Persistent

class Match(Persistent):
    def __init__(self, team1, team2):
        self.team1 = team1
        self.team2 = team2
        self.team1score = ""
        self.team2score = ""
    
    def __str__(self):
        return "{0} {1} - {2} {3}".format(self.team1, self.team1score, self.team2score, self.team2)
    
    def shortstr(self):
        return "{0}-{1}".format(self.team1score, self.team2score)
    
    def play(self):
        team1score = 0
        team2score = 0
        team1cards = copy.copy(self.team1.cards)
        team2cards = copy.copy(self.team2.cards)
        random.shuffle(team1cards)
        random.shuffle(team2cards)
        for card in range(25):
            card1 = team1cards[card]
            card2 = team2cards[card]
            if card1 > card2:
                team1score += 1
            elif card2 > card1:
                team2score += 1
        if team1score > team2score:
            self.winner = self.team1
        elif team2score > team1score:
            self.winner = self.team2
        else:
            self.winner = None
        self.team1score = team1score
        self.team2score = team2score

class LeagueMatch(Match):
    def play(self):
        Match.play(self)
        if self.team1score > self.team2score:
            self.team1.wins += 1
            self.team2.losses += 1
        elif self.team2score > self.team1score:
            self.team2.wins += 1
            self.team1.losses += 1
        else:
            self.team1.draws += 1
            self.team2.draws += 1
        self.team1.points_for += self.team1score
        self.team2.points_against += self.team1score
        self.team2.points_for += self.team2score
        self.team1.points_against += self.team2score
