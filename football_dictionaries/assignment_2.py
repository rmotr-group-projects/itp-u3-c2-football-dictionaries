from football_dictionaries.assignment_1 import players_as_dictionaries
from football_dictionaries.squads_data import SQUADS_DATA

def players_by_position(squads_list):
    result = players_as_dictionaries(squads_list)
    
    positions= {}

    for player in result:
        position_key = player['position']
        positions.setdefault(position_key , []) # stores the new info in new list
        positions[position_key].append(player)  
    
    return positions

