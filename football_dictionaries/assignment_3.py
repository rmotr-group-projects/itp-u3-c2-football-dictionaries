from football_dictionaries import squads_data
from football_dictionaries.assignment_1 import players_as_dictionaries


def players_by_country_and_position(squads_list):
    country_dict={}
    players=players_as_dictionaries(squads_list)
    for country_player in players:
        country=country_player['country']
        position=country_player['position']
        country_dict.setdefault(country,{})
        country_dict[country].setdefault(position,[])
        country_dict[country][position].append(country_player)
    return country_dict
    
