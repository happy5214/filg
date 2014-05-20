class Division(object):
    def __init__(self, teams):
        self.teams = teams
        self.teams.sort(key=lambda x: (x.points, x.point_diff, x.points_for), reverse=True)
    
    def sort_teams(self):
        self.teams.sort(key=lambda x: (x.points, x.point_diff, x.points_for), reverse=True)
        self.model.dataChanged.emit(self.model.index(0,0), self.model.index(len(self.teams), 7))
