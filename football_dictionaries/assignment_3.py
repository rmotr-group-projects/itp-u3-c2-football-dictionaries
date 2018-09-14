from .squads_data import SQUADS_DATA
from .assignment_2 import players_as_dictionaries

def players_by_country_and_position(SQUADS_DATA):
    
    players_by_country_dict = {}
    squads_list = players_as_dictionaries(SQUADS_DATA)
    #pprint(squads_list)
    
    for player in squads_list:
        
        print(player['country'])
        
        players_by_country_dict.setdefault(player['country'], {})
        players_by_country_dict[player['country']].setdefault(player['position'], [])
        players_by_country_dict[player['country']][player['position']].append(player)
        
    return players_by_country_dict
    