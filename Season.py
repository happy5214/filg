from persistent import Persistent

from PyQt4 import uic
from PyQt4.QtCore import pyqtProperty, pyqtSignal, QObject
from PyQt4.QtGui import QWidget

from LeagueModel import LeagueModel
from Division import Division

from Cup import *
from LeagueCupChampionsLeague import LeagueCupChampionsLeague
from TwoConferenceFourDivisionLeague import TwoConferenceFourDivisionLeague

class Season(QObject):
    def __init__(self, league):
        super(Season, self).__init__()
        self.league = league

class SixteenTeamDivisionalSeason(Season):
    played_round = pyqtSignal()
    league_finished = pyqtSignal()
    update_cup_seedings = pyqtSignal()
    
    def __init__(self, league, cup=SixteenTeamDivisionalCup()):
        super(SixteenTeamDivisionalSeason, self).__init__(league)
        self.league_wrapper = TwoConferenceFourDivisionLeague(league, self)
        self.cup_wrapper = SixteenTeamDivisionalCupWrapper(cup, self)
        self.champions_league = LeagueCupChampionsLeague()
        self.league_wrapper.league_finished.connect(self.champions_league.league_winner)
        self.cup_wrapper.cup_finished.connect(self.champions_league.cup_winner)
        self.init_widget()
        self.league_wrapper.round_played()
        self.update_cup_seedings.emit()
    
    def init_widget(self):
        self._v_widget = uic.loadUi("Season.ui")
        self.widget.setWindowTitle(self.name)
        self.widget.tabs.addTab(self.league_wrapper.widget, "League")
        self.widget.tabs.addTab(self.cup_wrapper.widget, "Cup")
        self.widget.tabs.addTab(self.champions_league.widget, "Champions League")
    
    @pyqtProperty(QWidget)
    def widget(self):
        return self._v_widget
    
    @pyqtProperty(dict)
    def divisions(self):
        return self.league_wrapper.divisions
    
