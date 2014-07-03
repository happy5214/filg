from PyQt4 import uic
from PyQt4.QtCore import pyqtProperty, pyqtSignal, QObject
from PyQt4.QtGui import QWidget

from TeamSeason import TeamSeason

from LeagueModel import LeagueModel

class TwoLevelLeague(QObject):
    played_round = pyqtSignal()
    league_finished = pyqtSignal(TeamSeason)
    update_cup_seedings = pyqtSignal()
    
    def __init__(self, first, second, season):
        super(TwoLevelLeague, self).__init__()
        self.first = first
        self.second = second
        self.season = season
        self.first_model = LeagueModel(first)
        self.second_model = LeagueModel(second)
        self.played_round.connect(self.round_played)
        self.init_widget()
        self.round_played()
    
    def init_widget(self):
        self._v_widget = uic.loadUi("TwoLevelLeague.ui")
        self.widget.leaguePlayButton.clicked.connect(self.play_round)
        self.widget.firstTable.setModel(self.first_model)
        self.widget.secondTable.setModel(self.second_model)
    
    @pyqtProperty(QWidget)
    def widget(self):
        return self._v_widget
    
    def round_played(self):
        self.widget.roundLabel.setText(str(self.first.round))
        self.first_model.dataChanged.emit(self.first_model.index(0,0), self.first_model.index(len(self.first.teams), 7))
        self.second_model.dataChanged.emit(self.second_model.index(0,0), self.second_model.index(len(self.second.teams), 7))
        self.update_cup_seedings.emit()
        if self.first.round == len(self.first.schedule):
            self.league_done()
        
    def play_round(self):
        self.first.play_round()
        self.second.play_round()
        self.played_round.emit()
    
    def league_done(self):
        self.widget.leaguePlayButton.setEnabled(False)
        winner = self.first.teams[0]
        self.league_finished.emit(winner)
    
