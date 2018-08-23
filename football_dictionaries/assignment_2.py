from squads_data import SQUADS_DATA
from assignment_1 import players_as_dictionaries

def players_by_position(SQUADS_DATA):
    squads_list=players_as_dictionaries(SQUADS_DATA)
    new_dict={}
    for player in squads_list:
        new_dict.setdefault(player['position'],[])
        new_dict[player['position']].append(player)
    return new_dict
    
