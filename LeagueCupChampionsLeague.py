from PyQt4 import uic
from PyQt4.QtCore import QObject
from PyQt4.QtGui import QWidget

class LeagueCupChampionsLeague(QObject):
    def __init__(self):
        super(LeagueCupChampionsLeague, self).__init__()
        self.widget = uic.loadUi("LeagueCupChampionsLeague.ui")
    
    def league_winner(self, winner):
        self.widget.leagueWinner.setText(str(winner))
    
    def cup_winner(self, winner):
        self.widget.cupWinner.setText(str(winner))
    
