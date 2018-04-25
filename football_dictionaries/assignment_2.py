from .assignment_1 import players_as_dictionaries

def players_by_position(squads_list):
    
    positions_dict = {}
    
    for player in players_as_dictionaries(squads_list):
        
        position = player['position']
        
        # if position not in positions_dict:
        #     positions_dict[position] = []
        
        positions_dict.setdefault(position, [])
            
        positions_dict[position].append(player)
            
    return positions_dict


