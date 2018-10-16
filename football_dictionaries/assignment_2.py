from .assignment_1 import players_as_dictionaries

def players_by_position(squads_list):
    player_as_dict = players_as_dictionaries(squads_list)
    dict_of_positions = {}
    for player in player_as_dict:
        position = player['position']
        dict_of_positions.setdefault(position, [])
        dict_of_positions[position].append(player)
    return dict_of_positions