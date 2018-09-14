from .squads_data import SQUADS_DATA
from .assignment_1 import players_as_dictionaries

def players_by_position(SQUADS_DATA):
    
    squads_list = players_as_dictionaries(SQUADS_DATA)
    dictionary_of_player_pos = {}
    
    for player in squads_list:
        
        dictionary_of_player_pos.setdefault(player["position"], [])
        dictionary_of_player_pos[player["position"]].append(player)
        
    return dictionary_of_player_pos