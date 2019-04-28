from .assignment_1 import players_as_dictionaries

def players_by_country_and_position(squads_list):
    results = {}
    squads_data = players_as_dictionaries(squads_list)
    for player in squads_data:
        country = player['country']
        position = player['position']
        results.setdefault(country, {})
        results[country].setdefault(position, [])
        results[country][position].append(player)
    
    return results