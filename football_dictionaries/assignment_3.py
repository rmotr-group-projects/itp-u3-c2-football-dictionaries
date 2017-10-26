from .assignment_1 import players_as_dictionaries

def players_by_country_and_position(squads_list):
    player_info = players_as_dictionaries(squads_list)
    player_country = {}
    for player in player_info:
        country = player["country"]
        pos = player["position"]
        player_country.setdefault(country, {})
        player_country[country].setdefault(pos, [])
        player_country[country][pos].append(player)
    return player_country  
