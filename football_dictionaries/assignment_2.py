from football_dictionaries.assignment_1 import players_as_dictionaries

def players_by_position(squads_list):
    
    playerlist = players_as_dictionaries(squads_list)
    
    position_dict = {}
    
    for player in playerlist:
        
        position = player['position']
        position_dict.setdefault(position, [])
        position_dict[position].append(player)
        
        
    return position_dict
        
