from persistent import Persistent

class TeamSeason(Persistent):
    def __init__(self, team):
        self.team = team
        self.wins = 0
        self.losses = 0
        self.draws = 0
        self.points_for = 0
        self.points_against = 0
    
    def __str__(self):
        return str(self.team)
    
    @property
    def cards(self):
        return self.team.cards
    
    @property
    def points(self):
        return self.wins * 3 + self.draws
    
    @property
    def point_diff(self):
        return self.points_for - self.points_against
    
    def season_to_str(self):
        print "{:<30}\t{:>5}\t{:>5}\t{:>5}\t{:>5}\t{:>5}\t{:>5}\t{:>5}".format(self, self.wins, self.losses, self.draws, self.points, self.points_for, self.points_against, self.point_diff)
