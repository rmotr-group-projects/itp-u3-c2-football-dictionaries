from .assignment_1 import players_as_dictionaries

def players_by_position(squads_list):
    #Uses previous assignment function for base
    new_squads_list = players_as_dictionaries(squads_list)
    player_position_dict = {}
    for player in new_squads_list:
        # Appends player dictionary to a new position dictionary
        player_position_dict.setdefault(player['position'], [])
        player_position_dict[player['position']].append(player)
    return player_position_dict




    
    
    
