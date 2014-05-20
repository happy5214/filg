from PyQt4 import uic
from PyQt4.QtCore import pyqtProperty, pyqtSignal, QObject
from PyQt4.QtGui import QWidget

from TeamSeason import TeamSeason

from LeagueModel import LeagueModel
from Division import Division

class TwoConferenceFourDivisionLeague(QObject):
    played_round = pyqtSignal()
    league_finished = pyqtSignal(TeamSeason)
    update_cup_seedings = pyqtSignal()
    
    def __init__(self, league, season):
        super(TwoConferenceFourDivisionLeague, self).__init__()
        self.league = league
        self.season = season
        self.league_model = LeagueModel(league)
        self.init_divisions()
        self.played_round.connect(self.round_played)
        self.init_widget()
    
    def init_widget(self):
        self._v_widget = uic.loadUi("TwoConferenceFourDivisionLeague.ui")
        self.widget.leaguePlayButton.clicked.connect(self.play_round)
        self.widget.leagueTable.setModel(self.league_model)
        self.widget.division1Table.setModel(self.division_models[self.season.division_names[0]])
        self.widget.division2Table.setModel(self.division_models[self.season.division_names[1]])
        self.widget.division3Table.setModel(self.division_models[self.season.division_names[2]])
        self.widget.division4Table.setModel(self.division_models[self.season.division_names[3]])
        self.widget.division1Group.setTitle(self.season.labels[0])
        self.widget.division2Group.setTitle(self.season.labels[1])
        self.widget.division3Group.setTitle(self.season.labels[2])
        self.widget.division4Group.setTitle(self.season.labels[3])
        self.widget.conference1Group.setTitle(self.season.labels[4])
        self.widget.conference2Group.setTitle(self.season.labels[5])
    
    @pyqtProperty(QWidget)
    def widget(self):
        return self._v_widget
    
    def round_played(self):
        self.widget.roundLabel.setText(str(self.league.round))
        self.league_model.dataChanged.emit(self.league_model.index(0,0), self.league_model.index(len(self.league.teams), 7))
        self.update_cup_seedings.emit()
        if self.league.round == len(self.league.schedule):
            self.league_done()
        
    def play_round(self):
        self.league.play_round()
        self.played_round.emit()
    
    def league_done(self):
        self.widget.leaguePlayButton.setEnabled(False)
        winner = self.league.teams[0]
        self.league_finished.emit(winner)
#    
#    def cup_done(self):
#        league_winner = self.widget.leagueWinner.text()
#        cup_winner = self.widget.cupWinner.text()
#        if league_winner == cup_winner:
#            league_second = self.league.teams[1]
#            self.widget.cupWinner.setText(str(league_second))
    
    def init_divisions(self):
        self.divisions = {}
        self.division_models = {}
        for k, v in self.season.division_defs.items():
            division = []
            for team in self.league.teams:
                if str(team) in v:
                    division.append(team)
            self.divisions[k] = Division(division)
            self.played_round.connect(self.divisions[k].sort_teams)
            self.division_models[k] = self.divisions[k].model = LeagueModel(self.divisions[k])
    
