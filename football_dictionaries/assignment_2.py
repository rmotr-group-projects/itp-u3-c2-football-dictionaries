from football_dictionaries.assignment_1 import players_as_dictionaries

def players_by_position(squads_list):
    
    position_dict = {}
    player_list = players_as_dictionaries(squads_list)
    
    for player in player_list:
        position_dict.setdefault(player['position'], [])
        position_dict[player['position']].append(player)
    
    return position_dict
