from .assignment_1 import players_as_dictionaries

def players_by_position(squads_list):
    
    squads_data = players_as_dictionaries(squads_list)
    
    players_by_position_dict = {}
    
    for player in squads_data:
        position_abr = player['position']
        players_by_position_dict.setdefault(position_abr, [])
        players_by_position_dict[position_abr].append(player)
    
    return players_by_position_dict