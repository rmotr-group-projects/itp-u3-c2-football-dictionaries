from football_dictionaries.assignment_1 import players_as_dictionaries
from football_dictionaries.assignment_2 import players_by_position

def players_by_country_and_position(squads_list):
    result = {}
    player_dict = players_as_dictionaries(squads_list)
    
    for player in player_dict:
        #goal is to put values in result dict of positions
        country = player['country']
        position = player['position']
        result.setdefault(country, {})
        result[country].setdefault(position, [])
        #goal is to get the player information of that position into the value of the position key
        result[country][position].append(player)
    return result
    

