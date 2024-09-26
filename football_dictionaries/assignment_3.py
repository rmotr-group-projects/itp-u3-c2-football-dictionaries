from football_dictionaries.assignment_1 import players_as_dictionaries
from pprint import pprint

def players_by_country_and_position(squads_list):
    player_list = players_as_dictionaries(squads_list)
    country_position_dict = {}
    
    for player in player_list:
        country = player['country']
        position = player['position']
        country_position_dict.setdefault(country, {})
        country_position_dict[country].setdefault(position,[])
        country_position_dict[country][position].append(player)
        
    return country_position_dict