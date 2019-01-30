from football_dictionaries.assignment_1 import players_as_dictionaries

def players_by_country_and_position(squads_list):
    squads_dict = players_as_dictionaries(squads_list)
    player_dict = {}
    for player in squads_dict:
        country = player['country']
        position = player['position']
        player_dict.setdefault(country, {})
        player_dict[country].setdefault(position, [])
        player_dict[country][position].append(player)
    return player_dict
