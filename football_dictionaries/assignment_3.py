
from football_dictionaries.assignment_1 import players_as_dictionaries
def players_by_country_and_position(squads_list):
    players = players_as_dictionaries(squads_list)
    result = {}   
    for player in players:
        country = player['country']
        position = player['position']
        result.setdefault(country, {})
        list_to_append = result[country].setdefault(position, [])
        list_to_append.append(player)
    return result
          


    
