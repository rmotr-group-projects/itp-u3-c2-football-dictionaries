from football_dictionaries.assignment_1 import players_as_dictionaries
from football_dictionaries.assignment_2 import players_by_position

def players_by_country_and_position(squads_list):
    player_dictionaries = players_as_dictionaries(squads_list)
    players_sorted_by_position = players_by_position(squads_list)
    
    result = {}
    
    for player_as_a_dict in player_dictionaries:
        country = player_as_a_dict['country']
        position = player_as_a_dict['position']
        result.setdefault(country, {})
        result[country].setdefault(position, [])
        
        result[country][position].append(player_as_a_dict)
            
    
    
    return result