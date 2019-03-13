from football_dictionaries.assignment_1 import players_as_dictionaries

def players_by_position(squads_list):
    players = players_as_dictionaries(squads_list)
    players_dict = {}
    for player in players:
        position = player['position']
        players_dict.setdefault(position,[])
        players_dict[position].append(player)
    return players_dict
