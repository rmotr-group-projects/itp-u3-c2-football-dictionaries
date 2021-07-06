from .assignment_1 import players_as_dictionaries


def players_by_country_and_position(squads_list):
    team = players_as_dictionaries(squads_list)
    by_players_country = {}
    
    for player in team:
        country = player['country']
        position = player['position']
        by_players_country.setdefault(country, {})
        by_players_country[country].setdefault(position, [])
        by_players_country[country][position].append(player)
    
    return by_players_country
