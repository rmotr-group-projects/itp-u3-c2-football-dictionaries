# Assignment 1
from squads_data import SQUADS_DATA
from assignment_1 import players_as_dictionaries

def players_by_position(squads_list):
    squash_dict = players_as_dictionaries(squads_list)
    result={}
    
    
    for dict_ in squash_dict:
        position = dict_['position']
        result.setdefault(position, [])
        result[position].append(dict_)
        
        
        
    
    return result


print(players_by_position(SQUADS_DATA))