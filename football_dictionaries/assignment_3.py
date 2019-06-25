
from pprint import pprint
from football_dictionaries.assignment_1 import players_as_dictionaries
from football_dictionaries.assignment_2 import players_by_position
from football_dictionaries.squads_data import SQUADS_DATA
def players_by_country_and_position(squads_list):
    pass
    result = {}
    for position, players in players_by_position(SQUADS_DATA).items():
        for player in players:
            country = player['country']
            position = player['position']
            result.setdefault(country, {})
            result[country].setdefault(position, [])
            result[country][position].append(player)
    return result
    
