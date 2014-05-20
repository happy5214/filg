import copy
import random

def gen_matches(teams):
    if type(teams) != list:
        teams = range(1,team_num+1)
    opps = {}
    for team in teams:
        opponents = []
        for opp in teams:
            if team != opp:
                opponents.append(opp)
        opps[team] = opponents
    matches = []
    for team, opponents in opps.items():
        for opp in opponents:
            matches.append((team,opp))
    return matches

def comparematches(match1, match2):
    (match1_1, match1_2) = match1
    if match1_1 in match2 or match1_2 in match2:
        return False
    return True

def findmatch(matches, rest):
    while True:
        poss = rest.pop(0)
        for match in matches:
            if not comparematches(match, poss):
                poss = None
                break
        if poss:
            return poss

def gen_round(match_num, matches):
    round = []
    try:
        random.shuffle(matches)
        round.append(matches.pop(0))
        poss = copy.copy(matches)
        for x in range(1,match_num):
            match = findmatch(round, poss)
            round.append(match)
            matches.remove(match)
        return round
    except IndexError:
        matches.extend(round)
        return gen_round(match_num, matches)

def gen_schedule(teams):
    match_num = 0
    round_num = 0
    rounds = []
    if type(teams) != list:
        match_num = teams / 2
        round_num = (teams - 1) * 2
    else:
        match_num = len(teams) / 2
        round_num = (len(teams) - 1) * 2
    matches = gen_matches(teams)
    for x in range(round_num):
        rounds.append(gen_round(match_num, matches))
    return rounds
