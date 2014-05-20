from persistent import Persistent

class Team(Persistent):
    def __init__(self, name, cards):
        self.name = name
        self.cards = cards
    
    def __str__(self):
        return self.name
