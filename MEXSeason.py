from Season import *
from TwoLevelLeague import TwoLevelLeague
from ThirtyTwoTeamUnseededCup import *

class MEXSeason(Season):
    name = "Mexico"
    
    league_finished = pyqtSignal()
    update_challenge_cup_seedings = pyqtSignal()
    
    def __init__(self, first, second, cup=ThirtyTwoTeamUnseededCup(teams = ["First", "Second"] * 16)):
        super(MEXSeason, self).__init__()
        self.league_wrapper = TwoLevelLeague(first, second, self)
        self.cup_wrapper = ThirtyTwoTeamUnseededCupWrapper(cup, self)
        self.league_wrapper.update_cup_seedings.connect(self.update_challenge_cup_seedings)
        #self.league_wrapper.league_finished.connect(self.champions_league.league_winner)
        self.league_wrapper.league_finished.connect(self.league_finished)
        self.init_widget()
    
    def init_widget(self):
        self.widget.tabs.addTab(self.cup_wrapper.widget, "Cup")
        self.widget.tabs.addTab(self.league_wrapper.widget, "League")
    
