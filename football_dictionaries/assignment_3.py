from .assignment_1 import players_as_dictionaries

def players_by_country_and_position(squads_list):
    player_as_dict = players_as_dictionaries(squads_list)
    dict_by_country = {}
    for player in player_as_dict:
        country = player['country']
        dict_by_country.setdefault(country, {})
        position = player['position']
        dict_by_country[country].setdefault(position, [])
        dict_by_country[country][position].append(player)
    return dict_by_country