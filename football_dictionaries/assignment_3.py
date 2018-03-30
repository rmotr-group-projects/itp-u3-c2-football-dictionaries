from .squads_data import SQUADS_DATA
from .assignment_1 import players_as_dictionaries
from pprint import pprint

def players_by_country_and_position(squads_list):
    country_dict = {}
    position_dict = {}
    players_dict = players_as_dictionaries(SQUADS_DATA)
    for player in players_dict:
        country = player['country']
        position = player['position']
        country_dict.setdefault(country, {})
        country_dict[country].setdefault(position, [])
        country_dict[country][position].append(player)
    return country_dict

pprint(players_by_country_and_position(SQUADS_DATA))