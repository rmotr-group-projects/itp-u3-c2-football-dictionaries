from .assignment_1 import players_as_dictionaries
    
def players_by_country_and_position(squads_list):
    data = players_as_dictionaries(squads_list)
    countries = {}
    for player in data:
        country = player['country']
        position = player['position']
        countries.setdefault(country, {})
        countries[country].setdefault(position, [])
        countries[country][position].append(player)
    return countries
    
