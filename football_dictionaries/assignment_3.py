from football_dictionaries.assignment_2 import player_to_dict

def players_by_country_and_position(squads_list):
    country_dict = {}
    for player in squads_list:
        player_dict = player_to_dict(player)
        country = player_dict['country']
        country_dict.setdefault(country, {})
        position = player_dict['position']
        country_dict[country].setdefault(position, [])
        country_dict[country][position].append(player_dict)
    return country_dict

