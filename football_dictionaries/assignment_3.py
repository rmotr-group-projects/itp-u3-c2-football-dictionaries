# Assignment 1
from football_dictionaries.assignment_1 import players_as_dictionaries
# Assignment 2
from football_dictionaries.assignment_2 import players_by_position

def players_by_country_and_position(squads_list):
    result = {} 
    list_of_player_dictionaries = players_as_dictionaries(squads_list)
    
    for player in list_of_player_dictionaries:
        country = player["country"]
        position = player["position"]
        result.setdefault(country, {})
        result[country].setdefault(position,[])
        result[country][position].append(player)
        
    return result 