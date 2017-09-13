from assignment_1 import players_as_dictionaries
from collections import OrderedDict

def players_by_country_and_position(squads_list):
    squad_list = players_as_dictionaries(squads_list)
    squads_by_country = OrderedDict()                                      
    
    for player in squad_list:
        player_country = player['country']
        player_position = player['position']
        squads_by_country.setdefault(player_country, {})
        squads_by_country[player_country].setdefault(player_position, [])
        squads_by_country[player_country][player_position].append(player)
        
    return squads_by_country