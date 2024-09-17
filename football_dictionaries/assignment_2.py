from assignment_1 import players_as_dictionaries

def players_by_position(squads_list):
    squads_dict = players_as_dictionaries(squads_list)
    by_position = {}
    for player in squads_dict:
        by_position.setdefault(player['position'], []) 
        by_position[player['position']].append(player)
    return by_position 
