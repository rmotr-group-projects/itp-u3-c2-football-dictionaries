from pprint import pprint 

from .assignment_1 import players_as_dictionaries
from .squads_data import SQUADS_DATA

def players_by_country_and_position(squads_list):
    
    result = {}
    
    player_json = players_as_dictionaries(squads_list)
    
    for player in player_json:
        result.setdefault(player['country'], {})
        result[player['country']].setdefault(player['position'], [])
        result[player['country']][player['position']].append(player)
    return result