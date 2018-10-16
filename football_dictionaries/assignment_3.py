from .assignment_1 import players_as_dictionaries
from .assignment_2 import players_by_position

def players_by_country_and_position(squads_list):
    
    countries_dict = {}
    
    for player in players_as_dictionaries(squads_list):
        
        country = player['country']
        position = player['position']
        
        # if country not in countries_dict:
        #     countries_dict[country] = {}
        countries_dict.setdefault(country, {})
            
        if position not in countries_dict[country]:
            countries_dict[country][position] = []
        
        countries_dict[country][position].append(player)
   
    return countries_dict