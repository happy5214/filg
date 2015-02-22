from persistent import Persistent

from PyQt4 import uic
from PyQt4.QtCore import pyqtProperty, pyqtSignal, QObject
from PyQt4.QtGui import QWidget

from Match import Match
from Team import Team
from TeamSeason import TeamSeason

class ThirtyTwoTeamUnseededCupWrapper(QObject):
    cup_finished = pyqtSignal([Team], [TeamSeason])
    
    def __init__(self, cup, season):
        super(ThirtyTwoTeamUnseededCupWrapper, self).__init__()
        self.cup = cup
        self.season = season
        self.init_widget()
        self.init_bracket()
        self.update_teams()
    
    def init_widget(self):
        self._v_widget = uic.loadUi("ThirtyTwoTeamUnseededCup.ui")
        self.widget.playCupMatchButton.clicked.connect(self.play_match)
    
    @pyqtProperty(QWidget)
    def widget(self):
        return self._v_widget
    
    @pyqtProperty(dict)
    def teams(self):
        return self.cup.teams
    
    def init_bracket(self):
        self.bracket = {(0,0): (self.widget.team1Score, self.widget.team2Score, self.widget.match1Team),
                        (0,1): (self.widget.team3Score, self.widget.team4Score, self.widget.match2Team),
                        (0,2): (self.widget.team5Score, self.widget.team6Score, self.widget.match3Team),
                        (0,3): (self.widget.team7Score, self.widget.team8Score, self.widget.match4Team),
                        (0,4): (self.widget.team9Score, self.widget.team10Score, self.widget.match5Team),
                        (0,5): (self.widget.team11Score, self.widget.team12Score, self.widget.match6Team),
                        (0,6): (self.widget.team13Score, self.widget.team14Score, self.widget.match7Team),
                        (0,7): (self.widget.team15Score, self.widget.team16Score, self.widget.match8Team),
                        (0,8): (self.widget.team17Score, self.widget.team18Score, self.widget.match9Team),
                        (0,9): (self.widget.team19Score, self.widget.team20Score, self.widget.match10Team),
                        (0,10): (self.widget.team21Score, self.widget.team22Score, self.widget.match11Team),
                        (0,11): (self.widget.team23Score, self.widget.team24Score, self.widget.match12Team),
                        (0,12): (self.widget.team25Score, self.widget.team26Score, self.widget.match13Team),
                        (0,13): (self.widget.team27Score, self.widget.team28Score, self.widget.match14Team),
                        (0,14): (self.widget.team29Score, self.widget.team30Score, self.widget.match15Team),
                        (0,15): (self.widget.team31Score, self.widget.team32Score, self.widget.match16Team),
                        (1,0): (self.widget.match1Score, self.widget.match2Score, self.widget.match17Team),
                        (1,1): (self.widget.match3Score, self.widget.match4Score, self.widget.match18Team),
                        (1,2): (self.widget.match5Score, self.widget.match6Score, self.widget.match19Team),
                        (1,3): (self.widget.match7Score, self.widget.match8Score, self.widget.match20Team),
                        (1,4): (self.widget.match9Score, self.widget.match10Score, self.widget.match21Team),
                        (1,5): (self.widget.match11Score, self.widget.match12Score, self.widget.match22Team),
                        (1,6): (self.widget.match13Score, self.widget.match14Score, self.widget.match23Team),
                        (1,7): (self.widget.match15Score, self.widget.match16Score, self.widget.match24Team),
                        (2,0): (self.widget.match17Score, self.widget.match18Score, self.widget.quarter1Team),
                        (2,1): (self.widget.match19Score, self.widget.match20Score, self.widget.quarter2Team),
                        (2,2): (self.widget.match21Score, self.widget.match22Score, self.widget.quarter3Team),
                        (2,3): (self.widget.match23Score, self.widget.match24Score, self.widget.quarter4Team),
                        (3,0): (self.widget.quarter1Score, self.widget.quarter2Score, self.widget.half1Team),
                        (3,1): (self.widget.quarter3Score, self.widget.quarter4Score, self.widget.half2Team),
                        (4,0): (self.widget.half1Score, self.widget.half2Score, self.widget.champions, self.widget.runnersUp)}
    
    def update_bracket(self):
        cup_index = tuple(self.cup.index)
        if cup_index == (0,-1):
            return
        matches = self.bracket.keys()
        matches.sort()
        for match in matches:
            self.match_played(match, (match == (4,0)))
            if match == cup_index:
                break
    
    def update_teams(self):
        self.widget.team1.setText(str(self.teams[0]))
        self.widget.team2.setText(str(self.teams[1]))
        self.widget.team3.setText(str(self.teams[2]))
        self.widget.team4.setText(str(self.teams[3]))
        self.widget.team5.setText(str(self.teams[4]))
        self.widget.team6.setText(str(self.teams[5]))
        self.widget.team7.setText(str(self.teams[6]))
        self.widget.team8.setText(str(self.teams[7]))
        self.widget.team9.setText(str(self.teams[8]))
        self.widget.team10.setText(str(self.teams[9]))
        self.widget.team11.setText(str(self.teams[10]))
        self.widget.team12.setText(str(self.teams[11]))
        self.widget.team13.setText(str(self.teams[12]))
        self.widget.team14.setText(str(self.teams[13]))
        self.widget.team15.setText(str(self.teams[14]))
        self.widget.team16.setText(str(self.teams[15]))
        self.widget.team17.setText(str(self.teams[16]))
        self.widget.team18.setText(str(self.teams[17]))
        self.widget.team19.setText(str(self.teams[18]))
        self.widget.team20.setText(str(self.teams[19]))
        self.widget.team21.setText(str(self.teams[20]))
        self.widget.team22.setText(str(self.teams[21]))
        self.widget.team23.setText(str(self.teams[22]))
        self.widget.team24.setText(str(self.teams[23]))
        self.widget.team25.setText(str(self.teams[24]))
        self.widget.team26.setText(str(self.teams[25]))
        self.widget.team27.setText(str(self.teams[26]))
        self.widget.team28.setText(str(self.teams[27]))
        self.widget.team29.setText(str(self.teams[28]))
        self.widget.team30.setText(str(self.teams[29]))
        self.widget.team31.setText(str(self.teams[30]))
        self.widget.team32.setText(str(self.teams[31]))
        self.update_bracket()
    
    def start_cup(self):
        self.widget.playCupMatchButton.setEnabled(True)
    
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
            self.widget.playCupMatchButton.setEnabled(False)
            self.cup_finished.emit(match.winner)

class ThirtyTwoTeamUnseededCup(Persistent):
    def __init__(self, **args):
        self.index = [0,-1]
        self.matches = [[Match("Team 1", "Team 2"), Match("Team 3", "Team 4"), Match("Team 5", "Team 6"), Match("Team 7", "Team 8"),
                         Match("Team 9", "Team 10"), Match("Team 11", "Team 12"), Match("Team 13", "Team 14"), Match("Team 15", "Team 16"),
                         Match("Team 17", "Team 18"), Match("Team 19", "Team 20"), Match("Team 21", "Team 22"), Match("Team 23", "Team 24"),
                         Match("Team 25", "Team 26"), Match("Team 27", "Team 28"), Match("Team 29", "Team 30"), Match("Team 31", "Team 32")],
                        [Match("Match 1 Winner", "Match 2 Winner"), Match("Match 3 Winner", "Match 4 Winner"),
                         Match("Match 5 Winner", "Match 6 Winner"), Match("Match 7 Winner", "Match 8 Winner"),
                         Match("Match 9 Winner", "Match 10 Winner"), Match("Match 11 Winner", "Match 12 Winner"),
                         Match("Match 13 Winner", "Match 14 Winner"), Match("Match 15 Winner", "Match 16 Winner")],
                        [Match("Match 17 Winner", "Match 18 Winner"), Match("Match 19 Winner", "Match 20 Winner"),
                         Match("Match 21 Winner", "Match 22 Winner"), Match("Match 23 Winner", "Match 24 Winner")],
                        [Match("Match 25 Winner", "Match 26 Winner"), Match("Match 27 Winner", "Match 28 Winner")],
                        [Match("Match 29 Winner", "Match 30 Winner")]]
        teams = list(map(lambda x: "Team " + str(x), range(1,33)))
        self.teams = args.get("teams", teams)
    
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
        for x in range(16):
            first_round[x].team1 = self.teams[x*2]
            first_round[x].team2 = self.teams[x*2+1]
    
