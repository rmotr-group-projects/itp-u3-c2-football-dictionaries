from football_dictionaries.assignment_1 import players_as_dictionaries

def players_by_position(squad):
    result = {}
    players_list = players_as_dictionaries(squad)
    for player in players_list:
        pos = player['position']
        result.setdefault(pos, [])
        result[pos].append(player)
    return result