from football_dictionaries.assignment_1 import players_as_dictionaries

def players_by_position(squads_list):
    squads_list = players_as_dictionaries(squads_list)
    position_dict = {}
    for player in squads_list:
        position = player['position']
        position_dict.setdefault(position, [])
        position_dict[position].append(player)
    
    return position_dict
