from pprint import pprint

from .assignment_1 import players_as_dictionaries
from .squads_data import SQUADS_DATA


def players_by_position(squads_list):
    result_dict = players_as_dictionaries(squads_list)
    result = {}
    for player in result_dict:
        result.setdefault(player['position'], [])
        result[player['position']].append(player)
    return result