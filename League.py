from persistent import Persistent

from Match import LeagueMatch
from TeamSeason import TeamSeason
from roundrobin import gen_schedule

class League(Persistent):
    def __init__(self, teams):
        self.mask_teams(teams)
        self.generate_matches()
    
    def mask_teams(self, teams):
        self.teams = []
        for team in teams:
            self.teams.append(TeamSeason(team))
    
    def generate_matches(self):
        self.fixtures = {}
        self.schedule = gen_schedule(self.teams)
        self.round = 0
    
    def play_round(self):
        round_matches = self.schedule[self.round]
        for teams in round_matches:
            match = LeagueMatch(teams[0], teams[1])
            match.play()
            self.fixtures[teams] = match
        self.round += 1
        self.teams.sort(key=lambda x: (x.points, x.point_diff, x.points_for), reverse=True)
    
    def print_season(self):
        print "After Round {0}:".format(self.round)
        print "{:<30}\t{:>5}\t{:>5}\t{:>5}\t{:>5}\t{:>5}\t{:>5}\t{:>5}".format("Team", "W", "L", "D", "Pts", "PF", "PA", "PD")
        for team in self.teams:
            team.season_to_str()
    
    def print_fixtures(self):
        for home in self.teams:
            for away in self.teams:
                if home == away or ((home,away) not in self.fixtures):
                    print "{:<5}".format(" "),
                    continue
                print "{:<5}".format(self.fixtures[(home, away)].shortstr()),
            print
