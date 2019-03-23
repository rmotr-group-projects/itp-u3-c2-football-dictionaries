from football_dictionaries import squads_data
from football_dictionaries.assignment_1 import players_as_dictionaries

def players_by_position(squads_list):
    position_dict={}
    squads_data=players_as_dictionaries(squads_list)
    for squad_pos in squads_data:
        position=squad_pos['position']
        position_dict.setdefault(position,[])
        position_dict[position].append(squad_pos)
    return position_dict
            
                
        
    
