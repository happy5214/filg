from PyQt4.QtCore import QAbstractTableModel, QModelIndex, QVariant, Qt

class LeagueModel(QAbstractTableModel):
    def __init__(self, league):
        super(LeagueModel, self).__init__()
        self.league = league
    
    def rowCount(self, parent):
        return len(self.league.teams)
    
    def columnCount(self, parent):
        return 8
    
    def data(self, index, role):
        if not(index.isValid()):
            return QVariant()
        if (role == Qt.DisplayRole):
            team = self.league.teams[index.row()]
            columns = (str(team), team.wins, team.losses, team.draws, team.points, team.points_for, team.points_against, team.point_diff)
            return columns[index.column()]
        else:
            return QVariant()
    
    def headerData(self, section, orientation, role):
        if (role != Qt.DisplayRole):
            return QVariant()
        
        if (orientation == Qt.Horizontal):
            columns = ("Team", "W", "L", "D", "Pts", "PF", "PA", "PD")
            return columns[section]
    
