from football_dictionaries.assignment_1 import players_as_dictionaries

def players_by_position(squads_list):
    res = {}
    playerdict = players_as_dictionaries(squads_list)
    for player in playerdict:
        res.setdefault(player['position'],[])
        res[player['position']].append(player)
    return res
