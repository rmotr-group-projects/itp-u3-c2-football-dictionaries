# Assignment 1
from football_dictionaries.assignment_1 import players_as_dictionaries
# Assignment 2
from football_dictionaries.assignment_2 import players_by_position

def players_by_country_and_position(squads_list):
    # sorted_by_position = players_by_position(squads_list)
    new_squad_list = players_as_dictionaries(squads_list)
    country_dict = {}
    
    for player in new_squad_list:
        country = player['country']
        country_dict.setdefault(country, {})
        position = player['position']
        country_dict[country].setdefault(position, [])
        country_dict[country][position].append(player) 
        
    return country_dict
