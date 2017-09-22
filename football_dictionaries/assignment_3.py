from .assignment_1 import players_as_dictionaries

def players_by_country_and_position(squads_list):
    by_pos = players_as_dictionaries(squads_list)
    dict_by_country = {}
    for player in by_pos:
        country = player['country']
        pos = player['position']
        dict_by_country.setdefault(country, {})
        dict_by_country[country].setdefault(pos, [])
        dict_by_country[country][pos].append(player)
    
    return dict_by_country
    
