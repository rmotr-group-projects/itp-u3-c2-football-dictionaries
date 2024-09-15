from football_dictionaries.assignment_2 import players_by_position
from football_dictionaries.assignment_1 import players_as_dictionaries
from football_dictionaries.squads_data import SQUADS_DATA

def players_by_country_and_position(squads_list):
    country_position = {}
    country = ''
    position = ''
    
    for player in players_as_dictionaries(squads_list):       
        country = player['country']
        position = player['position']        
        country_position.setdefault(country,{}) 
        country_position[country].setdefault(position, [])
        country_position[country][position].append(player)
    return country_position
    

    

print(players_by_country_and_position(SQUADS_DATA))



