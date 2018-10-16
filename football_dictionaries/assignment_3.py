from football_dictionaries.squads_data import SQUADS_DATA
from football_dictionaries.assignment_1 import players_as_dictionaries
from football_dictionaries.assignment_2 import players_by_position 


def players_by_country_and_position(squads_list):
    result = players_as_dictionaries(squads_list) 
    
    countries = {}
    
    for country in result: 
        
        country_key = country['country']
        position_key = country['position'] 
        
        countries.setdefault(country_key, {}) 
        countries[country_key].setdefault(position_key, [])
        countries[country_key][position_key].append(country)
    
    return countries
    
