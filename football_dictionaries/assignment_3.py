from .assignment_1 import players_as_dictionaries

def players_by_country_and_position(squads_list):
    squad = players_as_dictionaries(squads_list)
    players_by_country_dict = {}
    for player in squad:
        position = player['position']
        country = player['country']
        players_by_country_dict.setdefault(country, {})
        players_by_country_dict[country].setdefault(position, [])
        players_by_country_dict[country][position].append(player)
    
    return players_by_country_dict
    
