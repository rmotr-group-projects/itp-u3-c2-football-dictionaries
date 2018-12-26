from football_dictionaries.assignment_1 import players_as_dictionaries

def players_by_position(squads_list):
    result = {}
    players = players_as_dictionaries(squads_list)
    for player in players:
        position = player['position']
        result.setdefault(position, [])
        result[position].append(player)
    return result