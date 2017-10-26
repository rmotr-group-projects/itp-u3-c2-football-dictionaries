from pprint import pprint
from squads_data import SQUADS_DATA
from assignment_1 import players_as_dictionaries

def players_by_position(squads_list):
    squad = players_as_dictionaries(squads_list)
    by_position = {}
    
    for player in squad:
        position = player['position']
        by_position.setdefault(position, [])
        by_position[position].append(player)
    
    return by_position


#pprint(players_by_position(SQUADS_DATA))