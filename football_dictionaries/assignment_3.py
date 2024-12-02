from football_dictionaries.squads_data import SQUADS_DATA
from football_dictionaries.assignment_1 import players_as_dictionaries
def players_by_country_and_position(squads_list):
    squads_dict = players_as_dictionaries(squads_list)
#     print(squads_dict)
    result = {}
    for dict_ in squads_dict:
        country = dict_['country']
        position = dict_['position']
        result.setdefault(country, {})
        result[country].setdefault(position, [])
        result[country][position].append(dict_)
    return result


# print(players_by_country_and_position(SQUADS_DATA))