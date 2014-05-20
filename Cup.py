from persistent import Persistent

from PyQt4 import uic
from PyQt4.QtCore import pyqtProperty, pyqtSignal, QObject
from PyQt4.QtGui import QWidget

from Match import Match
from TeamSeason import TeamSeason

class SixteenTeamDivisionalCupWrapper(QObject):
    cup_finished = pyqtSignal(TeamSeason)
    
    def __init__(self, cup, season):
        super(SixteenTeamDivisionalCupWrapper, self).__init__()
        self.cup = cup
        self.season = season
        season.update_cup_seedings.connect(self.update_seedings)
        season.league_finished.connect(self.cup.fix_first_round)
#        self.cup_finished.connect(season.cup_done)
        self.init_widget()
        self.init_bracket()
    
    def init_widget(self):
        self._v_widget = uic.loadUi("SixteenTeamDivisionalCup.ui")
        self.widget.playCupMatchButton.clicked.connect(self.play_match)
        self.widget.division1Label.setText(self.season.labels[0])
        self.widget.division2Label.setText(self.season.labels[1])
        self.widget.division3Label.setText(self.season.labels[2])
        self.widget.division4Label.setText(self.season.labels[3])
        self.widget.conference1Label.setText(self.season.labels[4])
        self.widget.conference2Label.setText(self.season.labels[5])
        self.widget.division1Team.setText(self.season.placeholders[0])
        self.widget.division2Team.setText(self.season.placeholders[1])
        self.widget.division3Team.setText(self.season.placeholders[2])
        self.widget.division4Team.setText(self.season.placeholders[3])
        self.widget.conference1Team.setText(self.season.placeholders[4])
        self.widget.conference2Team.setText(self.season.placeholders[5])
        self.widget.division1Seed.setText(self.season.seeds[0])
        self.widget.division2Seed.setText(self.season.seeds[1])
        self.widget.division3Seed.setText(self.season.seeds[2])
        self.widget.division4Seed.setText(self.season.seeds[3])
        self.widget.conference1Seed.setText(self.season.seeds[4])
        self.widget.conference2Seed.setText(self.season.seeds[5])
    
    @pyqtProperty(QWidget)
    def widget(self):
        return self._v_widget
    
    @pyqtProperty(dict)
    def teams(self):
        return self.cup.teams
    
    def div_num(self, name):
        return self.season.division_names.index(name)
    
    def init_bracket(self):
        self.bracket = {(0,0): (self.widget.division1FirstScore, self.widget.division1FourthScore, self.widget.division1Team1, self.widget.division1Seed1),
                        (0,1): (self.widget.division1SecondScore, self.widget.division1ThirdScore, self.widget.division1Team2, self.widget.division1Seed2),
                        (0,2): (self.widget.division2FirstScore, self.widget.division2FourthScore, self.widget.division2Team1, self.widget.division2Seed1),
                        (0,3): (self.widget.division2SecondScore, self.widget.division2ThirdScore, self.widget.division2Team2, self.widget.division2Seed2),
                        (0,4): (self.widget.division3FirstScore, self.widget.division3FourthScore, self.widget.division3Team1, self.widget.division3Seed1),
                        (0,5): (self.widget.division3SecondScore, self.widget.division3ThirdScore, self.widget.division3Team2, self.widget.division3Seed2),
                        (0,6): (self.widget.division4FirstScore, self.widget.division4FourthScore, self.widget.division4Team1, self.widget.division4Seed1),
                        (0,7): (self.widget.division4SecondScore, self.widget.division4ThirdScore, self.widget.division4Team2, self.widget.division4Seed2),
                        (1,0): (self.widget.division1Score1, self.widget.division1Score2, self.widget.division1Team),
                        (1,1): (self.widget.division2Score1, self.widget.division2Score2, self.widget.division2Team),
                        (1,2): (self.widget.division3Score1, self.widget.division3Score2, self.widget.division3Team),
                        (1,3): (self.widget.division4Score1, self.widget.division4Score2, self.widget.division4Team),
                        (2,0): (self.widget.division1Score, self.widget.division2Score, self.widget.conference1Team),
                        (2,1): (self.widget.division3Score, self.widget.division4Score, self.widget.conference2Team),
                        (3,0): (self.widget.conference1Score, self.widget.conference2Score, self.widget.champions, self.widget.runnersUp)}
    
    def update_bracket(self):
        cup_index = tuple(self.cup.index)
        if cup_index == (0,-1):
            return
        matches = self.bracket.keys()
        matches.sort()
        for match in matches:
            self.match_played(match, (match == (3,0)))
            if match == cup_index:
                break
    
    def update_seedings(self):
        for k, v in self.season.divisions.items():
            self.teams[self.div_num(k)] = v.teams
        self.widget.division1FirstTeam.setText(str(self.teams[0][0]))
        self.widget.division1SecondTeam.setText(str(self.teams[0][1]))
        self.widget.division1ThirdTeam.setText(str(self.teams[0][2]))
        self.widget.division1FourthTeam.setText(str(self.teams[0][3]))
        self.widget.division2FirstTeam.setText(str(self.teams[1][0]))
        self.widget.division2SecondTeam.setText(str(self.teams[1][1]))
        self.widget.division2ThirdTeam.setText(str(self.teams[1][2]))
        self.widget.division2FourthTeam.setText(str(self.teams[1][3]))
        self.widget.division3FirstTeam.setText(str(self.teams[2][0]))
        self.widget.division3SecondTeam.setText(str(self.teams[2][1]))
        self.widget.division3ThirdTeam.setText(str(self.teams[2][2]))
        self.widget.division3FourthTeam.setText(str(self.teams[2][3]))
        self.widget.division4FirstTeam.setText(str(self.teams[3][0]))
        self.widget.division4SecondTeam.setText(str(self.teams[3][1]))
        self.widget.division4ThirdTeam.setText(str(self.teams[3][2]))
        self.widget.division4FourthTeam.setText(str(self.teams[3][3]))
        self.update_bracket()
    
    def play_match(self):
        finished = self.cup.play_match()
        index = tuple(self.cup.index)
        self.match_played(index, finished)
    
    def match_played(self, index, finished):
        matchLabels = self.bracket[index]
        match = self.cup.matches[index[0]][index[1]]
        matchLabels[0].setText(str(match.team1score))
        matchLabels[1].setText(str(match.team2score))
        matchLabels[2].setText(str(match.winner))
        if finished:
            if match.winner == match.team1:
                matchLabels[3].setText(str(match.team2))
            else:
                matchLabels[3].setText(str(match.team1))
#            self.widget.cupWinner.setText(str(match.winner))
            self.widget.playCupMatchButton.setEnabled(False)
            self.cup_finished.emit(match.winner)
        else:
            if index[0] == 0:
                seeds = ()
                if index[1] % 2 == 0:
                    seeds = ('1','4')
                else:
                    seeds = ('2','3')
                if match.winner == match.team1:
                    matchLabels[3].setText(seeds[0])
                else:
                    matchLabels[3].setText(seeds[1])

class SixteenTeamDivisionalCup(Persistent):
    def __init__(self):
        self.index = [0,-1]
        self.matches = [[Match("Division 1 First", "Division 1 Fourth"), Match("Division 1 Second", "Division 1 Third"),
                         Match("Division 2 First", "Division 2 Fourth"), Match("Division 2 Second", "Division 2 Third"),
                         Match("Division 4 First", "Division 4 Fourth"), Match("Division 4 Second", "Division 4 Third"),
                         Match("Division 4 First", "Division 4 Fourth"), Match("Division 4 Second", "Division 4 Third")],
                        [Match("Match 1 Winner", "Match 2 Winner"), Match("Match 3 Winner", "Match 4 Winner"),
                         Match("Match 5 Winner", "Match 6 Winner"), Match("Match 7 Winner", "Match 8 Winner")],
                        [Match("Division 1 Champion", "Division 2 Champion"), Match("Division 4 Champion", "Division 4 Champion")],
                        [Match("Conference 1 Champion", "Conference 2 Champion")]]
        self.teams = [ ["First", "Second", "Third", "Fourth"],
                       ["First", "Second", "Third", "Fourth"],
                       ["First", "Second", "Third", "Fourth"],
                       ["First", "Second", "Third", "Fourth"] ]
    
    def play_match(self):
        self.index[1] += 1
        round = self.matches[self.index[0]]
        match = None
        try:
            match = round[self.index[1]]
        except IndexError:
            self.index[0] += 1
            self.index[1] = 0
            round = self.matches[self.index[0]]
            match = round[0]
        winner = None
        while not winner:
            match.play()
            winner = match.winner
        try:
            next_match = self.matches[self.index[0] + 1][self.index[1] / 2]
            if self.index[1] % 2 == 0:
                next_match.team1 = winner
            else:
                next_match.team2 = winner
        except IndexError:
            return True
        
        return False
    
    def fix_first_round(self):
        first_round = self.matches[0]
        first_round[0].team1 = self.teams[0][0]
        first_round[0].team2 = self.teams[0][3]
        first_round[1].team1 = self.teams[0][1]
        first_round[1].team2 = self.teams[0][2]
        first_round[2].team1 = self.teams[1][0]
        first_round[2].team2 = self.teams[1][3]
        first_round[3].team1 = self.teams[1][1]
        first_round[3].team2 = self.teams[1][2]
        first_round[4].team1 = self.teams[2][0]
        first_round[4].team2 = self.teams[2][3]
        first_round[5].team1 = self.teams[2][1]
        first_round[5].team2 = self.teams[2][2]
        first_round[6].team1 = self.teams[3][0]
        first_round[6].team2 = self.teams[3][3]
        first_round[7].team1 = self.teams[3][1]
        first_round[7].team2 = self.teams[3][2]
    
